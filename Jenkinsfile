pipeline {
    agent any

    environment {
        IMAGE_NAME = "chatbot-app"
        TAG = "latest"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                sh 'docker build -t ${IMAGE_NAME}:${TAG} .'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'docker run --rm ${IMAGE_NAME}:${TAG} pytest'
            }
        }

        stage('Deploy') {
            steps {
                sh '''
                docker stop python-app || true
                docker rm python-app || true
                docker run -d -p 5000:5000 --name python-app ${IMAGE_NAME}:${TAG}
                '''
            }
        }
    }
}