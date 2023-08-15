# Harnessing Seamless Deployments: A Comprehensive Guide to AWS EC2 Instance Checker with CI/CD Integration

In the fast-paced world of DevOps, merging cloud resources with Continuous Integration/Continuous Deployment (CI/CD) is more than a fleeting trend—it's a transformative shift. Let's delve into the AWS EC2 Instance Checker, a prime example of this integration. Crafted using the Flask web framework, this tool bridges users to AWS EC2 instances and simplifies automated CI/CD deployments in Kubernetes.

As we journey through this exploration, we'll unpack the design, architecture, and synergy of modern DevOps tools. The driving principle? Learning by example is the most effective approach.

This guide serves two distinct audiences: Architects aiming to understand the structure and relationships in a microservice application integrated with CI/CD and GitOps, and the hands-on DevOps engineers looking to build their own pipelines using this guide as a foundation.

---

## Prerequisites

Before diving into the details of harnessing seamless deployments with the AWS EC2 Instance Checker and CI/CD integration, it's essential to ensure you're equipped with the foundational knowledge and tools. Here's a checklist to get you started:

1. **Basic Understanding of DevOps**: Familiarize yourself with the principles of DevOps, especially as it pertains to continuous integration and continuous deployment (CI/CD). 

2. **Kubernetes Knowledge**: Given that several sections of this guide delve into Kubernetes configurations and deployments, a basic understanding of Kubernetes is necessary. If you're new to Kubernetes, consider checking out the [official documentation](https://kubernetes.io/docs/concepts/overview/what-is-kubernetes/).

3. **Docker and Containers**: This guide often references Docker containers. Knowledge about containerization, especially using Docker, will be beneficial. For a refresher, see [Docker's official documentation](https://docs.docker.com/get-started/overview/).

4. **Git & GitHub**: Since we leverage GitHub Actions and other Git-based tools, familiarity with Git commands and GitHub's interface will be crucial. If you're new to Git, consider this [Git Basics Guide](https://git-scm.com/book/en/v2/Getting-Started-Git-Basics).

5. **AWS EC2 Basics**: As the primary focus of this guide is the AWS EC2 Instance Checker, understanding what AWS EC2 instances are and how they function can be beneficial. For an overview, check out [AWS's official EC2 documentation](https://docs.aws.amazon.com/AWSEC2/latest/UserGuide/concepts.html).

6. **Access to a Kubernetes Cluster**: To practically implement the steps in this guide, you'll need access to a Kubernetes cluster. This could be a local development cluster (like [Minikube](https://minikube.sigs.k8s.io/docs/start/)) or a cloud-based solution (like [AWS EKS](https://aws.amazon.com/eks/)).

7. **Required Software**: Ensure you have the necessary software installed or access to install them:
   - `kubectl` – Command-line tool for Kubernetes.
   - Docker – For building and managing containers.
   - Helm – For managing Kubernetes packages.
   - ArgoCD – For continuous delivery in Kubernetes.

8. **GitHub Account**: Since we utilize GitHub Actions, you'll need a GitHub account and repository to set up the CI/CD workflows.

9. **DockerHub Account**: For storing Docker images built through GitHub Actions, you'll need a DockerHub account.

Once you've familiarized yourself with the above essentials and ensured you have the necessary tools at your disposal, you're all set to delve into the guide!

---

Certainly! Here's a "Tool Alternatives" section that you can add to your guide:

---

## Tool Alternatives

In the realm of DevOps, while some tools have gained notable popularity and widespread adoption, it's always beneficial to be aware of alternative solutions. They might offer unique features or align better with specific project needs. Let's explore some popular alternatives to the tools mentioned in this guide:

1. **GitHub Actions Alternatives**:
   - **Jenkins**: A widely adopted open-source automation server that supports building, deploying, and automating any project.
   - **GitLab CI/CD**: Integrated CI/CD solution from GitLab.
   - **CircleCI**: A CI/CD platform that supports Docker and Kubernetes orchestration.
   - **Travis CI**: A cloud-based CI/CD service integrated with GitHub repositories.

2. **Argo CD Alternatives**:
   - **Flux**: A GitOps tool for Kubernetes, originally developed by Weaveworks.
   - **Jenkins X**: An open-source CI/CD solution for modern cloud applications on Kubernetes.
   - **Spinnaker**: A multi-cloud continuous delivery platform.

3. **Helm Alternatives**:
   - **Kustomize**: A standalone tool to customize Kubernetes objects through a kustomization file.
   - **Skaffold**: Handles the workflow for building, pushing, and deploying applications in Kubernetes.
   - **Terraform**: An infrastructure as code tool that supports provisioning of Kubernetes resources.

4. **Docker Hub Alternatives**:
   - **Quay.io**: A container image registry by Red Hat.
   - **Google Container Registry (GCR)**: Google's managed container image storage solution.
   - **Amazon Elastic Container Registry (ECR)**: AWS's managed Docker container registry.

Being aware of these alternatives allows teams to make informed decisions based on project requirements, existing toolchains, or personal preferences. Moreover, the vibrant landscape of DevOps tools ensures that there's a solution out there for every need, and sometimes mixing and matching tools from different ecosystems can lead to a highly optimized workflow.

---

## Diving into AWS EC2 Instance Checker

At its core, the AWS EC2 Instance Checker, powered by Python and Flask, serves as a gateway to AWS EC2 instances. Here's what it can do for you:

- **List EC2 Instances**: Fetch and display all your AWS EC2 instances.
- **Detail Specific Instances**: Dive deeper into specifics by selecting any instance.
- **Upgrade to IMDSv2**: Elevate the metadata service of your instances with just a click.
- **Verify Metadata Service Version**: Keep tabs on the metadata service version of each instance.

![App Architecture](img/CTO-APP.png)

---

## Modern CI/CD Tools: Synergy in Action

Central to the prowess of the AWS EC2 Instance Checker is its seamless integration with today's top CI/CD tools. Let's unpack the role of each tool in this ensemble:

### 1. GitHub Actions: The Heartbeat of Workflow Automation

Think of streamlining your software workflows right within GitHub; that's what GitHub Actions achieves. For our application, any changes to the `main` branch beckon GitHub Actions. It then crafts a Docker image and sends it to DockerHub.

### 2. Argo CD & Argo CD Image Updater: The Choreographers of Kubernetes Deployment

Enter Argo CD, a declarative, GitOps continuous delivery gem designed for Kubernetes. It shoulders the responsibility of ensuring our application's desired state (as defined in a Git repository) aligns with the Kubernetes cluster's actual state. Pair this with Argo CD Image Updater, and you're looking at a formidable duo that deploys and keeps Kubernetes manifests synchronized with the latest Docker images.

### 3. Helm: The Maestro of Kubernetes Package Management

Helm, recognized as Kubernetes' package manager, simplifies the intricacies of deployment. Our application's Helm chart outlines the Kubernetes resources in detail, enabling Argo CD to manage and update the application deployment effortlessly.

![CICD Pipline](img/CICD.png)

---

## The Symphony of Deployment

Navigating through buzzwords like CI/CD, ArgoCD, GitHub Actions, and Helm might feel overwhelming. But, we're here to demystify! Here's a simplified breakdown:

1. **Initialization**: ArgoCD syncs the Helm deployment in Kubernetes, marking GitHub as the definitive source.
2. **Commit & Build**: A developer's commit in the Python code activates GitHub Actions, which in turn crafts a container and propels it to Docker Hub.
3. **Monitor & Update**: Argo CD Image Updater keeps an eye on GitHub. On detecting a new container version, it tweaks the Helm charts, leading to an updated Kubernetes deployment.

This loop ensures consistent synchronization, with GitHub established as the source of truth.

For the Architects: You now have a robust overview of the entire structure, the relationships between components, and the CI/CD flow. With this understanding, you can make informed decisions and strategies for application deployment and scaling. If you're mainly interested in the higher-level architecture and design, you may choose to conclude your reading here.

For the Hands-On DevOps engineers : Continue on to delve deeper into the setup process and detailed instructions on building and managing this pipeline.

---

## Setting up Your DevOps Arsenal

Embarking on this DevOps journey requires some setup. Whether you're a seasoned developer or just starting, our guide will walk you through setting up the tools you need.

## Introduction

This guide provides a comprehensive walkthrough on setting up various tools, such as `kubectl`, `Helm`, `ArgoCD`, and more, on your Linux system. We aim to provide clear, concise, and in-depth instructions to cater to both novices and experts. If you already have tools like `kubectl` and a cluster set up, or any other steps completed, please feel free to skip the relevant installations and proceed to the sections you need.

## Table of Contents

- [Installation Procedures](#installation-procedures)
    - [Installing kubectl](#installing-kubectl)
    - [Installing Helm](#installing-helm)
    - [Installing argocd CLI](#installing-argocd-cli)
    - [Installing ArgoCD](#installing-argocd)
    - [Setting up ArgoCD Image updater](#setting-up-argocd-image-updater)
    - [Setting up GitHub Actions](#setting-up-github-actions)
- [Conclusion and Next Steps](#conclusion-and-next-steps)

## Installation Procedures

---

### Installing kubectl

For detailed information, refer to the official Kubernetes documentation [here](https://kubernetes.io/docs/tasks/tools/install-kubectl-linux/).

1. **Prepare your system**:
    ```bash
    sudo apt-get update
    sudo apt-get install -y ca-certificates curl
    ```

2. **Set up the Kubernetes apt repository**:
    ```bash
    sudo mkdir /etc/apt/keyrings
    echo "deb [signed-by=/etc/apt/keyrings/kubernetes-archive-keyring.gpg] https://apt.kubernetes.io/ kubernetes-xenial main" | sudo tee /etc/apt/sources.list.d/kubernetes.list
    ```

3. **Install `kubectl`**:
    ```bash
    sudo apt-get update
    sudo apt-get install -y kubectl
    ```

### Adding a New Context to `kubeconfig` for kubectl

After successfully installing `kubectl`, if you're working with multiple Kubernetes clusters, you might need to set up different contexts to switch seamlessly between these clusters.

1. **Prerequisites**:

    Ensure you have `kubectl` installed by checking its version:
    ```bash
    kubectl version
    ```

2. **Set up a new context**:
   
    Assume you've obtained credentials for a new Kubernetes cluster. To configure a new context, you need specifics about the cluster, user, and possibly a namespace.

    Firstly, define the cluster:
    ```bash
    kubectl config set-cluster <CLUSTER_NAME> --server=<CLUSTER_ENDPOINT> --certificate-authority=<PATH_TO_CA>
    ```

    Next, provide user credentials:
    ```bash
    kubectl config set-credentials <USER_NAME> --client-key=<PATH_TO_CLIENT_KEY> --client-certificate=<PATH_TO_CLIENT_CERT>
    ```

    Finally, create the context using the defined cluster and user:
    ```bash
    kubectl config set-context <CONTEXT_NAME> --cluster=<CLUSTER_NAME> --user=<USER_NAME>
    ```

3. **Verify your new context**:

    To ensure your context is properly established, view it with:
    ```bash
    kubectl config get-contexts
    ```

    If your newly added context appears in the list, you can activate it using:
    ```bash
    kubectl config use-context <CONTEXT_NAME>
    ```

Remember, by establishing various contexts in your `kubeconfig`, you can efficiently manage and alternate between multiple Kubernetes clusters. Always keep your `kubeconfig` files in a secure location, as they hold crucial access details. 

---

### Installing Helm

For detailed information, refer to the Helm's official guide [here](https://helm.sh/docs/intro/install/).

1. **Setup the Helm repository**:
    ```bash
    curl https://baltocdn.com/helm/signing.asc | gpg --dearmor | sudo tee /usr/share/keyrings/helm.gpg > /dev/null
    sudo apt-get install apt-transport-https --yes
    echo "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/helm.gpg] https://baltocdn.com/helm/stable/debian/ all main" | sudo tee /etc/apt/sources.list.d/helm-stable-debian.list
    ```

2. **Install Helm**:
    ```bash
    sudo apt-get update
    sudo apt-get install helm
    ```

---

### Installing ArgoCD CLI

For detailed information, check out the ArgoCD official documentation [here](https://argo-cd.readthedocs.io/en/stable/getting_started/).

1. **Download and install latest ArgoCD version**:
    ```bash
    curl -sSL -o argocd-linux-amd64 https://github.com/argoproj/argo-cd/releases/latest/download/argocd-linux-amd64
    sudo install -m 555 argocd-linux-amd64 /usr/local/bin/argocd
    rm argocd-linux-amd64
    ```

---

### Installing ArgoCD
For detailed information, refer to the ArgoCD's official guide [here](https://argo-cd.readthedocs.io/en/stable/getting_started/).

1. **Create a new namespace for ArgoCD**:
    ```bash
    kubectl create namespace argocd
    ```

2. **Install ArgoCD into the created namespace**:
    ```bash
    kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj/argo-cd/stable/manifests/install.yaml
    ```

3. **Change the `argocd-server` service type to `LoadBalancer`**:
    ```bash
    kubectl patch svc argocd-server -n argocd -p '{"spec": {"type": "LoadBalancer"}}'
    ```

4. **Retrieve the initial admin secret**:
    ```bash
    kubectl get secrets -n argocd argocd-initial-admin-secret -o yaml
    echo "<-secret-string->" | base64 -d
    ```

5. **Login to ArgoCD**:
   
   First, get the `EXTERNAL-IP` of the `argocd-server`:
   ```bash
   kubectl get service -n argocd argocd-server
   ```
   
   Use the obtained IP or hostname to login:
   ```bash
   sudo argocd login <ARGOCD_SERVER> --insecure
   ```

   The `--insecure` flag is used to disable server certificate validation. This is useful when connecting to an ArgoCD server that does not have a trusted certificate (e.g., self-signed). While it simplifies the login process, it's essential to understand that by skipping the certificate validation, you may be susceptible to "man-in-the-middle" attacks. In a production environment, you should aim to use a valid SSL/TLS certificate for ArgoCD to avoid using this flag.

6. **Verify the ArgoCD installation**:
    ```bash
    argocd version
    ```

    The output should resemble:
    ```
    argocd: v2.8.0+804d4b8
      BuildDate: 2023-08-07T19:41:16Z
      GitCommit: 804d4b8ca6bc4c2cf02c5c971aa923ec5b8623f0
      GitTreeState: clean
      GoVersion: go1.20.6
      Compiler: gc
      Platform: linux/amd64
    argocd-server: v2.8.0+804d4b8
      BuildDate: 2023-08-07T14:25:33Z
      GitCommit: 804d4b8ca6bc4c2cf02c5c971aa923ec5b8623f0
      GitTreeState: clean
      GoVersion: go1.20.6
      Compiler: gc
      Platform: linux/amd64
      Kustomize Version: v5.1.0 2023-06-19T16:58:18Z
      Helm Version: v3.12.1+gf32a527
      Kubectl Version: v0.24.2
      Jsonnet Version: v0.20.0
    ```

7. **Update the ArgoCD password**:
    ```bash
    argocd account update-password
    ```

With these steps, you should have ArgoCD installed and configured on your Kubernetes cluster. Adjust any specific commands or values based on your unique setup and requirements.

---

### Setting up ArgoCD Image Updater
For detailed information, refer to the ArgoCD's Image Updater official guide [here](https://argocd-image-updater.readthedocs.io/en/stable/).

1. **Install ArgoCD Image Updater**:
    ```bash
    kubectl apply -n argocd -f https://raw.githubusercontent.com/argoproj-labs/argocd-image-updater/stable/manifests/install.yaml
    ```

2. **Configure Logging Level for Troubleshooting**:
   
   Edit the `argocd-image-updater-config` ConfigMap to set the desired log level:
   ```yaml
   data:
     log.level: debug
   ```

3. **Verify the Logs**:
   
   After you've set up the Image Updater, you can inspect its logs to ensure everything's running correctly:
   ```bash
   kubectl -n argocd logs argocd-image-updater-<POD_NAME>
   ```

   Ideally, the logs should indicate no applications are using the Image Updater yet.

   ```bash
   time="2023-08-15T08:06:06Z" level=info msg="Processing results: applications=1 images_considered=0 images_skipped=0 images_updated=0 errors=0"
   ```

4. **Authorize Image Updater to Update GitHub Image Versions**:

   For this, you need to create a Kubernetes secret with your GitHub username and personal access token. You can create and manage personal access tokens in GitHub by following [this guide](https://docs.github.com/en/enterprise-server@3.6/authentication/keeping-your-account-and-data-secure/managing-your-personal-access-tokens).
   
   Store the GitHub credentials in environment variables:
   ```bash
   export GITHUB_USER=<YOUR_USERNAME>
   export GITHUB_TOKEN=<YOUR_GITHUB_TOKEN>
   ```

   Create the necessary secret in Kubernetes:
   ```bash
   kubectl --namespace argocd \
       create secret generic git-creds \
       --from-literal=username=$GITHUB_USER \
       --from-literal=password=$GITHUB_TOKEN
   ```

5. **Define an Application using a Manifest**:

   Now, create the ArgoCD application referencing the GitHub credentials to utilize the ArgoCD Image Updater. Make sure the manifest aligns with your project's specifics:
   
   ```yaml
      apiVersion: argoproj.io/v1alpha1
      kind: Application
      metadata:
        name: aws-ec2-instance-checker
        namespace: argocd
        annotations:
          argocd-image-updater.argoproj.io/image-list: fdervisi/aws-ec2-instance-checker:*
          argocd-image-updater.argoproj.io/write-back-method: git:secret:argocd/git-creds
          argocd-image-updater.argoproj.io/git-branch: master
      spec:
        project: default
        source:
          repoURL: https://github.com/fdervisi/k8s_cicd_overview
          targetRevision: HEAD
          path: helm/aws-ec2-instance-checker
        destination:
          server: https://kubernetes.default.svc
          namespace: aws-ec2-instance-checker
        syncPolicy:
          automated:
            prune: true
            selfHeal: true
            allowEmpty: true
   ```

    After saving the manifest, apply it to Kubernetes:

    ```bash
    kubectl apply -f argocd-app.yaml
    ```

    This command will instruct Kubernetes to create the resources defined in the `argocd-app.yaml` file. If the Application already exists, it will be updated with the new specifications from the file.


6. **Validate the Configuration**:
   
   You can recheck the logs after setting up the application:
   ```bash
   kubectl -n argocd logs argocd-image-updater-<POD_NAME>
   ```

   After setting up an application, you should see logs indicating that the Image Updater is processing an application:

   ```bash
   time="2023-08-15T08:06:06Z" level=info msg="Processing results: applications=1 images_considered=1 images_skipped=0 images_updated=1 errors=0"
   ```

   And verify the application in argocd using:
   ```bash
   argocd app list
   ```

   After applying the manifest to Kubernetes and allowing ArgoCD a moment to synchronize, you can see the new application reflected in the ArgoCD GUI.

   And this is how it looks like in the ArgoCD graphical user interface:
   ![App Architecture](img/argoCD.png)

7. **Understanding the Argo CD Image Updater Behavior**:

   When Argo CD Image Updater updates an application, it creates or updates a specific configuration file within the designated repository to track the updated image version. For example, with the setup you've defined:

   The Image Updater will write a file named `.argocd-source-aws-ec2-instance-checker.yaml` in the `helm` directory of your repository. This file will look something like:

   ```yaml
   helm:
     parameters:
     - name: image.name
       value: fdervisi/aws-ec2-instance-checker
       forcestring: true
     - name: image.tag
       value: 6.0.0
       forcestring: true
   ```

   This file is instrumental for Argo CD to understand which image and tag should be deployed for the specified application. It's crucial to ensure that this file is either included in the repository (for tracking) or excluded based on your CI/CD preferences.

---

### Setting up GitHub Actions

Setting up GitHub Actions requires a few setup steps. The following guide provides a basic overview of integrating Docker with GitHub Actions for an example repository:

1. **Docker Credentials with GitHub Actions**:

   Before setting up the GitHub Action workflow, you need to securely provide your Docker credentials to GitHub Actions. Follow the steps below:

   - **Navigate to your GitHub repository**.
   - Open the repository **Settings**.
   - Navigate to **Secrets and variables > Actions**.
   - Click on **New repository secret**.
   - Create a new secret named **DOCKERHUB_USERNAME** and set its value to your Docker ID.
   - Create a new Personal Access Token (PAT) for Docker Hub.
   - Add this PAT as another secret in your GitHub repository with the name **DOCKERHUB_TOKEN**.

   [Further Reading on Docker Credentials in GitHub Actions](https://docs.docker.com/build/ci/github-actions/)

2. **GitHub Action Workflow Setup**:

   To set up a GitHub Action to build a Docker image and push it to Docker Hub whenever there's a push to the master branch, follow these steps:

   - **Navigate to your GitHub repository**.
   - Go to the **Actions** tab.
   - Click on **New Workflow** and choose a template, or set up your custom workflow. Below is an example `.yml` file for the described action:

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
       - name: Check Out Code
         uses: actions/checkout@v2

       - name: Log in to DockerHub
         uses: docker/login-action@v1
         with:
           username: ${{ secrets.DOCKERHUB_USERNAME }}
           password: ${{ secrets.DOCKERHUB_TOKEN }}

       - name: Build and Push Docker Image
         uses: docker/build-push-action@v2
         with:
           context: aws-ec2-instance-checker
           push: true
           tags: |
             fdervisi/aws-ec2-instance-checker:${{ github.run_number }}.0.0
             fdervisi/aws-ec2-instance-checker:latest
   ```

3. **Commit and Push Your Workflow**:

   After configuring your workflow, commit and push it to your repository. GitHub Actions will automatically recognize the `.yml` file and start the defined workflow whenever the triggering event occurs (in this case, a push to the master branch affecting the `aws-ec2-instance-checker` directory).

---

## Final Reflections

Integrating the AWS EC2 Instance Checker within a proficient CI/CD pipeline showcases the transformative power of today's deployment methodologies. Each code update sets into motion a streamlined process: the application is meticulously built, containerized, and seamlessly deployed to a Kubernetes cluster. This embodies the very core of GitOps—guaranteeing that the code you introduce is faithfully represented in production.

As you engage with these tools and strategies, it's imperative to stay informed with the latest developments, embrace best practices, and draw inspiration from community discussions. Ensure that credentials and sensitive information are securely managed, avoiding direct embedding in your code or configurations.

So, what's next? We encourage you to experiment further, perhaps by exploring the tool alternatives mentioned or by scaling and optimizing your CI/CD pipelines. Seek out communities and forums related to DevOps to keep learning and sharing. Remember, the field of DevOps is ever-evolving, and continuous learning is the key to harnessing its full potential.

Here's to the future of seamless deployments, enhanced security, and the evolving landscape of DevOps!