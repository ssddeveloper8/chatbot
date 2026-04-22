pipeline {
    agent any

    environment {
        IMAGE_NAME = "chatbot-app"
        TAG = "latest"
    }

    stages {

        stage('Build Docker Image') {
            steps {
                bat 'docker build -t %IMAGE_NAME%:%TAG% .'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker run --rm %IMAGE_NAME%:%TAG% pytest'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                docker stop python-app || exit 0
                docker rm python-app || exit 0
                docker run -d -p 5000:5000 --name python-app %IMAGE_NAME%:%TAG%
                '''
            }
        }
    }
}