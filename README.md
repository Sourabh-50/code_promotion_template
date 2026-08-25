# Enterprise Code Promotion Template

Welcome to the **Enterprise Code Promotion Template**. This repository serves as a complete, production-ready blueprint for implementing continuous integration, automated deployment, and continuous verification (CV) using modern DevOps practices.

## 🏗️ Architecture Overview

This template includes a full-stack application and a robust monitoring stack:

- **Backend:** A high-performance Python FastAPI service.
- **Frontend:** A lightweight Nginx-based static web interface.
- **Observability:** Prometheus and Grafana pre-configured to track live hardware metrics (CPU & Memory).
- **Orchestration:** Local Kubernetes cluster support (`kind`) for deployment testing.
- **CI/CD:** Designed specifically for **Harness CI/CD**, featuring automated rollbacks, manual approval gates, and continuous verification.

## 🚀 Getting Started Locally

### Prerequisites
- [Docker & Docker Compose](https://www.docker.com/)
- [Kubernetes / Kind](https://kind.sigs.k8s.io/)
- Python 3.9+ (for local backend development)

### 1. Spin up the Local Environment
To start the entire stack (Backend, Frontend, Prometheus, and Grafana), run:
```bash
docker-compose build --no-cache
docker-compose up -d
```

### 2. Access the Services
Once the stack is running, you can access the following services:
- **Frontend App:** [http://localhost:8080](http://localhost:8080)
- **Backend API Docs:** [http://localhost:8080/docs](http://localhost:8080/docs)
- **Prometheus UI:** [http://localhost:9090](http://localhost:9090)
- **Grafana Dashboards:** [http://localhost:3000](http://localhost:3000) *(Default Login: `admin` / `admin`)*

### 3. Monitoring & Dashboards
This repository includes a pre-provisioned Grafana dashboard that automatically tracks exact hardware metrics via the Python `psutil` library. 
To view it:
1. Open Grafana at `http://localhost:3000`.
2. Navigate to **Dashboards**.
3. Open the **CodeProm Health (Live Architecture)** dashboard.

## ♾️ Harness CI/CD Integration

This repository is optimized for deployment via **Harness**. The pipeline configuration supports:

1. **Automated Triggers:** Executes deployments automatically on GitHub pushes.
2. **Kubernetes Delegate:** Securely deploys manifests to your target cluster.
3. **Manual Approval Gates:** Pauses pipeline execution to require enterprise sign-off before hitting production.
4. **Continuous Verification (CV):** Leverages the `system_cpu_usage_percent` Prometheus metric to monitor health immediately after a rollout. If CPU spikes dangerously, Harness will automatically rollback the deployment.

## 📂 Repository Structure

```text
.
├── backend/                  # FastAPI Application, Dockerfile, and requirements
├── frontend/                 # Static HTML/JS frontend and Dockerfile
├── infrastructure/           # Kubernetes manifests (frontend, backend, harness config)
├── monitoring/               # Grafana dashboards and Prometheus configuration
├── docker-compose.yml        # Local orchestration stack
└── README.md                 # You are here!
```

## 🛠️ Modifying the Application

To add new hardware metrics or modify the backend API, edit `backend/main.py`. The built-in Prometheus Instrumentator will automatically expose any new custom `Gauge` or `Counter` metrics you define to the `/metrics` endpoint.

---
*Built with ❤️ for Enterprise DevOps Teams.*
