# AWS EC2 Instance Checker Application: A Complete Overview

AWS EC2 Instance Checker is a simple yet comprehensive application built using the Flask web framework and designed to interact with AWS EC2 instances. The application, combined with the power of modern DevOps tools like Argo CD, Argo CD Image Updater, and GitHub Actions, showcases an efficient and automated end-to-end CI/CD deployment in a Kubernetes environment.

## Application Architecture and Functionalities

The AWS EC2 Instance Checker application has been developed in Python, leveraging the Flask web framework to provide a user-friendly interface. The core functionalities of the application include:

- **Listing all EC2 instances**: The application connects to AWS EC2 service and retrieves information about all instances.
- **Displaying detailed information about a specific instance**: Users can select a specific instance to see more detailed information.
- **Enabling the Instance Metadata Service Version 2 (IMDSv2) on a specific instance**: Users have the option to upgrade the metadata service of an instance to IMDSv2.
- **Verifying if an instance is using IMDSv1**: The application verifies the metadata service version for each EC2 instance.

Internally, the application uses the `boto3` library to interact with AWS and the `requests` library to send HTTP requests. It also uses an Open Policy Agent (OPA) server for policy enforcement related to the EC2 instances' metadata service versions.

The application is packaged into a Docker image for easy and consistent deployment, which is particularly beneficial when deploying the application to different environments.

![App Architecture](img/CTO-APP.png)


## Integration with CI/CD Tools

To streamline the deployment process, this project adopts a modern, automated deployment pipeline using tools such as GitHub Actions, Argo CD, Argo CD Image Updater, and Helm.

### GitHub Actions

GitHub Actions helps to automate software development workflows directly in GitHub. For this project, it is utilized to automatically build a Docker image of the application and push it to DockerHub whenever there's a change pushed to the `main` branch.

### Argo CD and Argo CD Image Updater

Argo CD is a declarative, GitOps continuous delivery tool for Kubernetes. It's used in this project to automate the deployment of the application to a Kubernetes cluster. With Argo CD, the state of the Kubernetes cluster can be synchronized with the desired state defined in a Git repository.

Argo CD Image Updater is an add-on component to Argo CD that aids in automatically updating the container image versions in the Kubernetes manifests. When a new Docker image is available in DockerHub, Argo CD Image Updater modifies the image tag in the Helm chart, thus triggering Argo CD to synchronize the changes and update the application in the Kubernetes cluster.

### Helm

Helm is a package manager for Kubernetes that simplifies the deployment and management of applications. The Helm chart included in the project outlines the Kubernetes resources required to run the application, allowing Argo CD to efficiently manage and update the application deployment.

## Putting it All Together

The synergy of these tools and practices demonstrates an effective CI/CD pipeline for a Kubernetes application. With each commit pushed to the GitHub repository, the application is automatically built, containerized, and deployed to a Kubernetes cluster. All changes to the application are automatically synchronized with the running application in Kubernetes, ensuring consistency between the application code and the application running in the production environment. This automatic synchronization represents the GitOps principles at work, enhancing the speed, security, and stability of the deployment process.

![CICD Pipline](img/CICD.png)













Detailes instructions:

# README.md

---

## Install kubectl

Kubernetes control, also known as `kubectl`, is a command-line tool for communicating with a Kubernetes cluster. Follow the steps below to set it up on a Linux system.

🔗 [Official Installation Guide](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/)

### 1. Update the apt package index and install packages for Kubernetes apt repository:

```bash
sudo apt-get update
sudo apt-get install -y ca-certificates curl
```

### 2. Download the Google Cloud public signing key:

```bash
sudo mkdir /etc/apt/keyrings
echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
```

### 3. Install `kubectl`:

```bash
sudo apt-get update
sudo apt-get install -y kubectl
```

---

## Install Helm

Helm, the Kubernetes package manager, simplifies deploying and managing applications on Kubernetes.

🔗 [Official Installation Guide](https://helm.sh/docs/intro/install/)

For Debian/Ubuntu systems:

```bash
curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
sudo apt-get install apt-transport-https --yes
echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
sudo apt-get update
sudo apt-get install helm
```

---

## Install argocd CLI tool

ArgoCD is a declarative, GitOps continuous delivery tool for Kubernetes. To interact with ArgoCD from the command line, we'll need the `argocd` CLI tool.

```bash
curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
rm argocd-linux-amd64
```

### Install ArgoCD on your Cluster:

```bash
kubectl create namespace argocd
kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
```

To access ArgoCD externally, change the `argocd-server` service type to `LoadBalancer`:

```bash
kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
```

### Accessing ArgoCD:

To access the initial password for ArgoCD:

```bash
kubectl get secrets -n argocd argocd-initial-admin-secret -o yaml
```

Decoding the password:

```bash
echo "<-secret-string->" | base64 -d
```

Use the username `admin` and the decoded password to log in:

```bash
argocd login <ARGOCD_SERVER> --insecure
```

For example:

```bash
argocd login argocd.api.server.com --username admin --password mypassword- --insecure
```

### Post Installation:

After successfully logging in, verify the installed versions:

```bash
argocd version
```

You should also update the default password and delete the secret `argocd-initial-admin-secret`:

```bash
argocd account update-password
```

---

## GitHub Actions for Docker Builds

To automate the Docker image build and push process, GitHub Actions can be a powerful tool.

### Docker Credentials:

To interact with Docker Hub using GitHub Actions, you'll need to set up credentials. Here's a step-by-step guide:

1. Navigate to your GitHub repository.
2. Access the repository Settings -> Secrets and variables -> Actions.
3. Add a new secret named `DOCKERHUB_USERNAME` with your Docker ID as its value.
4. Create a [Personal Access Token (PAT) for Docker Hub](https://docs.docker.com/build/ci/github-actions/).
5. Add the PAT as another secret in your repository with the name `DOCKERHUB_TOKEN`.

### GitHub Action Configuration:

The YAML configuration below is part of the repository and automates the build and push process for a Docker image:

```yaml
name: Build and Push Docker Image

on:
  push:
    branches: [ master ]
    paths:
    - 'aws-ec2-instance-checker/**'

jobs:
  build:
    runs-on: ubuntu-latest
    steps:
    ...
```
