pipeline {
    agent any

    environment {
        DOCKER_USERNAME = credentials('docker-username')
        DOCKER_PASSWORD = credentials('docker-password')
        GITOPS_REPO = 'https://github.com/YOUR-USERNAME/gitops-repo.git'
        GITOPS_CREDENTIALS = 'gitops-token' // Jenkins credential with write access
    }

    stages {
        stage('Checkout') {
            steps {
                checkout scm
            }
        }

        stage('Run Tests') {
            steps {
                sh 'pip install -r app/requirements.txt pytest'
                sh 'pytest app/test_main.py'
            }
        }

        stage('Build Docker Image') {
            steps {
                script {
                    IMAGE_TAG = sh(script: "date +%Y%m%d%H%M%S", returnStdout: true).trim()
                    sh "docker build -t $DOCKER_USERNAME/service-monitor:$IMAGE_TAG ."
                }
            }
        }

        stage('Push Docker Image') {
            steps {
                withCredentials([usernamePassword(credentialsId: 'docker-creds', passwordVariable: 'PASS', usernameVariable: 'USER')]) {
                    sh "echo $PASS | docker login -u $USER --password-stdin"
                    sh "docker push $DOCKER_USERNAME/service-monitor:$IMAGE_TAG"
                }
            }
        }

        stage('Update GitOps Repo') {
            steps {
                sshagent(['gitops-token']) {
                    sh """
                    git clone $GITOPS_REPO gitops-repo
                    cd gitops-repo
                    sed -i 's|tag:.*|tag: $IMAGE_TAG|' helm/go-monitor/values.yaml
                    git add helm/go-monitor/values.yaml
                    git commit -m "Update image tag to $IMAGE_TAG [ci skip]"
                    git push origin main
                    """
                }
            }
        }
    }
}