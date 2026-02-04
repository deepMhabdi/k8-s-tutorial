# Kubernetes Full-Stack Deployment Tutorial

Hands-on guide to deploy a **Flask backend** + **Express.js frontend** full-stack application on Kubernetes. Perfect for learning containerization, microservices, deployments, services, and ingress routing.

## 🎯 Project Overview

This repository demonstrates deploying a complete web application with:

- **Backend**: Flask API (Python)
- **Frontend**: Express.js / Node.js single-page app
- **Kubernetes**: Deployments, Services, ConfigMaps, and Ingress

The app consists of a frontend that communicates with a backend API, showcasing service discovery and inter-pod communication.

## 🏗️ Architecture

Frontend (Express.js) → Backend (Flask API) → Database (optional)
↓
Kubernetes Services + Ingress

text

## 🛠 Prerequisites

- Docker installed
- kubectl configured
- Kubernetes cluster (Minikube, kind, Docker Desktop, or cloud)
- Helm (optional, for ingress)
- `git` to clone the repo

## 🚀 Quick Start

### 1. Clone & Prepare

```bash
git clone https://github.com/deepMhabdi/k8-s-tutorial.git
cd k8-s-tutorial

2. Build Docker Images

Backend:

bash
cd backend
docker build -t flask-backend:latest .
docker tag flask-backend:latest <your-registry>/flask-backend:latest  # Push to registry if needed
cd ..

Frontend:

bash
cd frontend
docker build -t express-frontend:latest .
docker tag express-frontend:latest <your-registry>/express-frontend:latest
cd ..

3. Deploy to Kubernetes

bash
# Create namespace
kubectl create namespace k8s-tutorial

# Deploy backend
kubectl apply -f k8s/backend-deployment.yaml -n k8s-tutorial
kubectl apply -f k8s/backend-service.yaml -n k8s-tutorial

# Deploy frontend
kubectl apply -f k8s/frontend-deployment.yaml -n k8s-tutorial
kubectl apply -f k8s/frontend-service.yaml -n k8s-tutorial

# Optional: Deploy ingress
kubectl apply -f k8s/ingress.yaml -n k8s-tutorial

4. Verify Deployment

bash
kubectl get pods,deployments,services -n k8s-tutorial

# Check logs
kubectl logs deployment/flask-backend -n k8s-tutorial
kubectl logs deployment/express-frontend -n k8s-tutorial

# Port-forward to test
kubectl port-forward svc/frontend-service 3000:80 -n k8s-tutorial

Open http://localhost:3000 to see your app!
📁 Repository Structure

text
k8s-tutorial/
├── backend/                 # Flask API
│   ├── app.py
│   ├── requirements.txt
│   └── Dockerfile
├── frontend/                # Express.js Frontend
│   ├── server.js
│   ├── package.json
│   └── Dockerfile
├── k8s/                     # Kubernetes manifests
│   ├── backend-deployment.yaml
│   ├── backend-service.yaml
│   ├── frontend-deployment.yaml
│   ├── frontend-service.yaml
│   └── ingress.yaml
└── README.md

🔍 Key Kubernetes Concepts Covered
Component	File	Purpose
Deployment	*-deployment.yaml	Manages replicas & rolling updates
Service	*-service.yaml	Load balancing & service discovery
ConfigMap	(optional)	External configuration
Ingress	ingress.yaml	External HTTP routing
🧪 Practice Exercises

    Scale Frontend: kubectl scale deployment express-frontend --replicas=3

    Update Backend: Change image tag → kubectl rollout status deployment/flask-backend

    Test Service Discovery: Frontend calls backend via service name (backend-service)

    Debugging: Use kubectl logs, kubectl describe, kubectl exec

🧰 Useful Commands

bash
# Namespace operations
kubectl get all -n k8s-tutorial

# Cleanup
kubectl delete namespace k8s-tutorial

# Rollout history
kubectl rollout history deployment/flask-backend -n k8s-tutorial

# Port forward backend directly
kubectl port-forward svc/backend-service 5000:5000 -n k8s-tutorial

🌐 Access Your App
Method	URL
Port-forward	http://localhost:3000
Minikube	minikube service frontend-service -n k8s-tutorial
Ingress	<your-ingress-domain>
🚀 Next Steps

    Add PersistentVolume for data storage

    Deploy Redis/PostgreSQL as additional services

    Set up Horizontal Pod Autoscaler

    Configure CI/CD with GitHub Actions

    Add monitoring (Prometheus + Grafana)

🤝 Contributing

    Fork the repo

    Create feature branch

    Test your changes locally

    Submit PR

📄 License

MIT License - feel free to use and modify!

text

**Copy the entire block above** (from ```markdown to the closing ```) and paste it directly into your `README.md` file. 

This README is:
- ✅ **Ready to paste** (complete Markdown)
- ✅ **Professional** & user-friendly
- ✅ **Matches your Flask + Express structure**
- ✅ **Includes all common Kubernetes patterns**
- ✅ **Has quick-start that works**

Just update image tags, service names, and ports to match your exact YAML files! 🚀
