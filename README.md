# Kubernetes Tutorial Lab Environment

A hands‑on tutorial repository to learn Kubernetes fundamentals by deploying, scaling, and managing containerized applications on a local or cloud‑based Kubernetes cluster.

## 📌 Overview

This repository contains step‑by‑step labs and manifests to help you:

- Set up a local Kubernetes cluster (e.g., Minikube, kind, or Docker Desktop).
- Deploy sample applications using `Deployment`, `Service`, and `ConfigMap`.
- Scale workloads and explore rolling updates.
- Use basic monitoring and debugging tools (`kubectl logs`, `kubectl describe`, etc.).

All manifests are written in plain YAML and kept as simple as possible for beginners.

## 🛠 Prerequisites

Before you start, make sure you have:

- `kubectl` installed and configured.
- A running Kubernetes cluster (Minikube, kind, Docker Desktop, or cloud‑managed cluster).
- `git` installed to clone this repo.
- Basic familiarity with containers and Docker (optional but helpful).

## 🚀 Quick Start

1. Clone the repository:

   ```bash
   git clone https://github.com/deepMhabdi/k8-s-tutorial.git
   cd k8-s-tutorial

    Verify your cluster is ready:

    bash
    kubectl cluster-info
    kubectl get nodes

    Deploy the sample application:

    bash
    kubectl apply -f manifests/deployment.yaml
    kubectl apply -f manifests/service.yaml

    Check that the pods are running:

    bash
    kubectl get pods
    kubectl get services

    Access the application (if using Minikube):

    bash
    minikube service <service-name>

📁 Repository Structure

text
k8-s-tutorial/
├── manifests/            # Kubernetes YAML manifests
│   ├── deployment.yaml   # Application deployment
│   ├── service.yaml      # Service exposing the app
│   └── configmap.yaml    # Optional configuration
├── docs/                 # Additional guides and diagrams (if any)
└── README.md             # This file

Adjust paths and filenames to match what’s actually in your repo.
🧪 Labs and Exercises

Each lab focuses on a core Kubernetes concept:

    Lab 1 – Deploying an App: Use Deployment and Service to run a simple web app.

    Lab 2 – Scaling: Scale replicas and observe load distribution.

    Lab 3 – Rolling Updates: Update the app image and watch a rolling update.

    Lab 4 – Debugging: Practice common troubleshooting commands.

Each lab directory (if present) includes:

    A short description.

    The required YAML files.

    Step‑by‑step instructions.

🧰 Useful Commands

Here are some handy kubectl commands you’ll use throughout the tutorial:

bash
# List all pods
kubectl get pods

# Describe a pod
kubectl describe pod <pod-name>

# View logs
kubectl logs <pod-name>

# Delete a deployment
kubectl delete deployment <deployment-name>

# Apply all manifests in a directory
kubectl apply -f manifests/

🤝 Contributing

Contributions are welcome! If you want to:

    Add new labs or examples.

    Fix typos or improve explanations.

    Add multi‑language support or diagrams.

Please:

    Fork the repository.

    Create a feature branch (git checkout -b feature/your-feature).

    Commit your changes.

    Push to the branch and open a pull request.

📄 License

This project is open‑source and available under the MIT License. See the LICENSE file for details.
