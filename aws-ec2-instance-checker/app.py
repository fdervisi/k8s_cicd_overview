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
    """
    Converts datetime objects to string format recursively in a dictionary or list.

    Args:
        data (dict or list): The data to be converted..

    Returns:
        dict or list: The converted data.
    """
    if isinstance(data, dict):
        return {k: datetime_to_string(v) for k, v in data.items()}
    elif isinstance(data, list):
        return [datetime_to_string(v) for v in data]
    elif isinstance(data, datetime.datetime):
        return data.isoformat()
    else:
        return data


@app.route('/', methods=['GET', 'POST'])
def ec2_instances():
    """
    Renders the instances.html template with a list of EC2 instances.

    Returns:
        str: The rendered HTML template.
    """
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

                        instance_data = datetime_to_string({
    'id': instance.id,
    'name': name,
    'state': instance.state['Name'],
    'type': instance.instance_type,
    'public_ip': instance.public_ip_address
})
            opa_response = requests.post(f'{OPA_URL}/v1/data/ec2/result', json={"input": instance_data})
            is_public_exposed = opa_response.json().get('result', False)

            instances_list.append({
                'id': instance.id,
                'name': name,
                'state': instance.state['Name'],
                'type': instance.instance_type,
                'public_ip': instance.public_ip_address,
                'is_public_exposed': is_public_exposed
            })
        
        print("instance_data", instance_data)
        print("opa_response", opa_response.json())

        return render_template('instances.html', instances=instances_list)
    
    return render_template('index.html')

@app.route('/instance/<id>', methods=['GET'])
def instance(id):
    """
    Returns the details of an EC2 instance with the given ID.

    Args:
        id (str): The ID of the EC2 instance.

    Returns:
        dict: The details of the EC2 instance in JSON format.
    """
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


if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)