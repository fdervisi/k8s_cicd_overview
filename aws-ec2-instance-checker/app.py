import os
from flask import Flask, request, render_template, jsonify, session
from flask_session import Session
import boto3
import requests
import datetime

app = Flask(__name__)
app.config['SESSION_TYPE'] = 'filesystem'
app.config['SECRET_KEY'] = 'your-secret-key'
Session(app)

OPA_URL = os.getenv('OPA_URL')

def datetime_to_string(data):
    if isinstance(data, dict):
        return {k: datetime_to_string(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [datetime_to_string(v) for v in data]
    elif isinstance(data, datetime.datetime):
        return data.isoformat()
    else:
        return data

def check_security_group_rules(instance_id):
    access_key = session.get('access_key')
    secret_key = session.get('secret_key')
    region = session.get('region')
    
    aws_session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    
    ec2 = aws_session.client('ec2')
    response = ec2.describe_instances(
        InstanceIds=[
            instance_id,
        ]
    )

    instance_data = datetime_to_string(response['Reservations'][0]['Instances'][0])
    opa_response = requests.post(f'{OPA_URL}/v1/data/ec2/securitygroups', json={"input": instance_data})
    
    result = opa_response.json().get('deny', [])
    has_overly_permissive_sg = len(result) > 0

    return has_overly_permissive_sg, result

@app.route('/', methods=['GET', 'POST'])
def ec2_instances():
    if request.method == 'POST':
        session['access_key'] = request.form['access_key']
        session['secret_key'] = request.form['secret_key']
        session['region'] = request.form['region']
        
        access_key = session.get('access_key')
        secret_key = session.get('secret_key')
        region = session.get('region')
        
        aws_session = boto3.Session(
            aws_access_key_id=access_key,
            aws_secret_access_key=secret_key,
            region_name=region
        )
        
        ec2 = aws_session.resource('ec2')
        instances = ec2.instances.all()
        
        instances_list = []
        for instance in instances:
            name = ''
            if instance.tags is not None:
                for tag in instance.tags:
                    if tag['Key'] == 'Name':
                        name = tag['Value']
            has_overly_permissive_sg, reasons = check_security_group_rules(instance.id)
            instances_list.append({
                'id': instance.id,
                'name': name,
                'state': instance.state['Name'],
                'type': instance.instance_type,
                'public_ip': instance.public_ip_address,
                'has_overly_permissive_sg': has_overly_permissive_sg,
                'exposed_reasons': reasons
            })
        
        return render_template('instances.html', instances=instances_list)
    
    return render_template('index.html')

@app.route('/instance/<id>', methods=['GET'])
def instance(id):
    access_key = session.get('access_key')
    secret_key = session.get('secret_key')
    region = session.get('region')
    
    aws_session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    
    ec2 = aws_session.client('ec2')
    response = ec2.describe_instances(
        InstanceIds=[
            id,
        ]
    )

    return jsonify(response)

@app.route('/enable_imdsv2/<id>', methods=['POST'])
def enable_imdsv2(id):
    access_key = session.get('access_key')
    secret_key = session.get('secret_key')
    region = session.get('region')
    
    aws_session = boto3.Session(
        aws_access_key_id=access_key,
        aws_secret_access_key=secret_key,
        region_name=region
    )
    
    ec2 = aws_session.client('ec2')
    try:
        ec2.modify_instance_metadata_options(
            InstanceId=id,
            HttpTokens='required',
            HttpEndpoint='enabled'
        )
        return jsonify(success=True)
    except Exception as e:
        print(e)
        return jsonify(success=False)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
