pipeline {
    agent any
    environment {
        DOCKERHUB = 'amthul/bookreview-app'
        KUBECONFIG = 'C:\\Users\\Administrator\\.kube\\config'
    }
    stages {
        stage('Checkout') {
            steps {
                git credentialsId: 'github-pat', url: 'https://github.com/MUQEETh1233/book-review-about.git'
            }
        }
        stage('Build Docker Image') {
            steps {
                script {
                    docker.build("${DOCKERHUB}:latest")
                }
            }
        }
        stage('Push to Docker Hub') {
            steps {
                script {
                    docker.withRegistry('', 'dockerhub-credentials') {
                        docker.image("${DOCKERHUB}:latest").push()
                    }
                }
            }
        }
        stage('Deploy to Kubernetes') {
            steps {
                bat 'kubectl apply -f deployment.yaml'
                bat 'kubectl apply -f service.yaml'
            }
        }
    }
    triggers {
        pollSCM('* * * * *')
    }
}
