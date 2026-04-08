# Service Monitor

## Overview
Service Monitor is a Python-based microservice for monitoring system metrics and service reliability.  
This repo contains the application, Docker setup, tests, and CI/CD workflow to build and push images.

## Tech Stack
- **Language:** Python 3.11  
- **Containerization:** Docker / Podman  
- **CI/CD:** GitHub Actions (build, test, push, update GitOps repo)  
- **Testing:** Pytest  
- **Kubernetes Testing:** Kind (local cluster)

## Features
- Collects and exposes service metrics via REST API.  
- Containerized for easy deployment.  
- Automated tests run on each push.  
- CI/CD pipeline builds Docker image and updates GitOps repo with latest image tag.

## Workflow
1. Code pushed to `main` branch triggers Jenkins Pipeline.  
2. Dependencies installed and tests executed.  
3. Docker image built and pushed to Docker Hub.  
4. GitOps repository `values.yaml` updated with new image tag automatically.  
5. Helm deployment can use the updated tag for deployment.

## Local Testing
- Used **Kind** to spin up a local Kubernetes cluster.  
- Application container tested with local `kubectl` and port-forwarding.  

## Jenkins
- `Jenkinsfile` handles:  
  - Build & push Docker image  
  - Run unit tests  
  - Update GitOps repo image tag