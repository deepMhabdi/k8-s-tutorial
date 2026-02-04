Kubernetes (K8s) Tutorial 🚀
A comprehensive hands-on tutorial for learning Kubernetes from basics to advanced concepts. This repository contains practical examples, configurations, and applications to help you master container orchestration with Kubernetes.
📋 Table of Contents

About
Prerequisites
Getting Started
Project Structure
Topics Covered
Installation
Usage
Examples
Contributing
Resources
License

🎯 About
This tutorial provides a practical approach to learning Kubernetes by walking through real-world examples and use cases. Whether you're a beginner starting with containers or an experienced developer looking to understand K8s orchestration, this guide has something for everyone.
✅ Prerequisites
Before starting this tutorial, you should have:

Basic understanding of Docker and containerization
Familiarity with command-line interface (CLI)
Basic knowledge of YAML syntax
Understanding of basic networking concepts

Required Tools

Docker: Container runtime (version 20.0 or higher)
kubectl: Kubernetes command-line tool
minikube or kind: Local Kubernetes cluster (for development)
Python: Version 3.8+ (for running examples)
Git: For cloning the repository

🚀 Getting Started
1. Clone the Repository
bashgit clone https://github.com/deepMhabdi/k8-s-tutorial.git
cd k8-s-tutorial
2. Set Up Local Kubernetes Cluster
Using Minikube
bash# Start minikube
minikube start --driver=docker

# Verify cluster is running
kubectl cluster-info
kubectl get nodes
Using kind (Kubernetes in Docker)
bash# Create a cluster
kind create cluster --name k8s-tutorial

# Verify cluster
kubectl cluster-info --context kind-k8s-tutorial
3. Verify Installation
bash# Check kubectl version
kubectl version --client

# Check cluster status
kubectl get all --all-namespaces
📁 Project Structure
k8-s-tutorial/
├── deep/                    # Main tutorial content
│   ├── basics/             # Basic Kubernetes concepts
│   ├── deployments/        # Deployment configurations
│   ├── services/           # Service examples
│   ├── networking/         # Networking configurations
│   ├── storage/            # Persistent storage examples
│   └── advanced/           # Advanced topics
├── examples/               # Practical examples
│   ├── python-app/        # Sample Python application
│   └── web-app/           # Sample web application
├── configs/               # Kubernetes configuration files
├── scripts/               # Helper scripts
└── README.md             # This file
📚 Topics Covered
Fundamentals

🐳 Kubernetes Architecture
📦 Pods and Containers
🏷️ Labels and Selectors
🔧 ConfigMaps and Secrets
📝 Namespaces

Workloads

🚀 Deployments
📊 ReplicaSets
🔄 StatefulSets
⚡ DaemonSets
📋 Jobs and CronJobs

Networking

🌐 Services (ClusterIP, NodePort, LoadBalancer)
🔌 Ingress Controllers
🔐 Network Policies
🌍 DNS in Kubernetes

Storage

💾 Volumes
📀 Persistent Volumes (PV)
📋 Persistent Volume Claims (PVC)
🗄️ Storage Classes

Advanced Topics

📈 Horizontal Pod Autoscaling
🔍 Monitoring and Logging
🔒 RBAC (Role-Based Access Control)
🛡️ Security Best Practices
🎯 Resource Quotas and Limits

💻 Installation
Install kubectl
macOS:
bashbrew install kubectl
Linux:
bashcurl -LO "https://dl.k8s.io/release/$(curl -L -s https://dl.k8s.io/release/stable.txt)/bin/linux/amd64/kubectl"
sudo install -o root -g root -m 0755 kubectl /usr/local/bin/kubectl
Windows:
powershellchoco install kubernetes-cli
Install Minikube
macOS:
bashbrew install minikube
Linux:
bashcurl -LO https://storage.googleapis.com/minikube/releases/latest/minikube-linux-amd64
sudo install minikube-linux-amd64 /usr/local/bin/minikube
Windows:
powershellchoco install minikube
🎮 Usage
Running Your First Pod
bash# Create a simple nginx pod
kubectl run nginx-pod --image=nginx:latest

# Check pod status
kubectl get pods

# Get detailed information
kubectl describe pod nginx-pod

# Delete the pod
kubectl delete pod nginx-pod
Deploying from YAML Files
bash# Apply a configuration
kubectl apply -f configs/deployment.yaml

# View deployments
kubectl get deployments

# View services
kubectl get services

# Delete resources
kubectl delete -f configs/deployment.yaml
Working with Examples
bash# Navigate to example directory
cd examples/python-app

# Build Docker image
docker build -t python-k8s-app:latest .

# Apply Kubernetes configurations
kubectl apply -f k8s/

# Check deployment status
kubectl get all
📖 Examples
Example 1: Simple Web Application
Deploy a basic web application with a service:
yaml# See examples/web-app/deployment.yaml for full example
apiVersion: apps/v1
kind: Deployment
metadata:
  name: web-app
spec:
  replicas: 3
  selector:
    matchLabels:
      app: web
  template:
    metadata:
      labels:
        app: web
    spec:
      containers:
      - name: web
        image: nginx:latest
        ports:
        - containerPort: 80
Example 2: Python Application with Database
Deploy a Python application connected to a database:
bashcd examples/python-app
kubectl apply -f k8s/
kubectl get pods -w
Common Commands Cheat Sheet
bash# Get cluster information
kubectl cluster-info

# List all resources
kubectl get all

# List pods
kubectl get pods
kubectl get pods -o wide

# Logs
kubectl logs <pod-name>
kubectl logs -f <pod-name>  # Follow logs

# Execute commands in pod
kubectl exec -it <pod-name> -- /bin/bash

# Port forwarding
kubectl port-forward <pod-name> 8080:80

# Scale deployment
kubectl scale deployment <name> --replicas=5

# Update deployment
kubectl set image deployment/<name> container=image:tag

# Rollout status
kubectl rollout status deployment/<name>
kubectl rollout history deployment/<name>

# Delete resources
kubectl delete pod <pod-name>
kubectl delete deployment <deployment-name>
🤝 Contributing
Contributions are welcome! Please feel free to submit a Pull Request. For major changes, please open an issue first to discuss what you would like to change.
How to Contribute

Fork the repository
Create your feature branch (git checkout -b feature/AmazingFeature)
Commit your changes (git commit -m 'Add some AmazingFeature')
Push to the branch (git push origin feature/AmazingFeature)
Open a Pull Request

📚 Resources
Official Documentation

Kubernetes Official Documentation
kubectl Cheat Sheet
Kubernetes API Reference

Learning Resources

Kubernetes Basics Tutorial
Play with Kubernetes
Kubernetes Patterns Book

Community

Kubernetes Slack
Kubernetes GitHub
CNCF Community

📝 License
This project is licensed under the MIT License - see the LICENSE file for details.
👨‍💻 Author
Deep Mhabdi

GitHub: @deepMhabdi
