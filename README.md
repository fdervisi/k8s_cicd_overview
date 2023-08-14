# CTO Wizard Application: A Complete Overview

CTO Wizard is a simple yet comprehensive application built using the Flask web framework and designed to interact with AWS EC2 instances. The application, combined with the power of modern DevOps tools like Argo CD, Argo CD Image Updater, and GitHub Actions, showcases an efficient and automated end-to-end CI/CD deployment in a Kubernetes environment.

## Application Architecture and Functionalities

The CTO Wizard application has been developed in Python, leveraging the Flask web framework to provide a user-friendly interface. The core functionalities of the application include:

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