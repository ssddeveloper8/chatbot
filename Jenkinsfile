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
                docker ps -a -q -f name=python-app > temp.txt
                set /p container=<temp.txt

                if not "%container%"=="" (
                    docker stop python-app
                    docker rm python-app
                )

                docker run -d -p 5000:5000 --name python-app %IMAGE_NAME%:%TAG%
                '''
            }
        }
    }
}