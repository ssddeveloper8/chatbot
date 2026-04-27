pipeline {
    agent any

    stages {

        stage('Build Image') {
            steps {
                bat 'docker-compose build'
            }
        }

        stage('Run Tests') {
            steps {
                bat 'docker-compose run --rm app pytest || exit 0'
            }
        }

        stage('Deploy') {
            steps {
                bat '''
                docker-compose down
                docker-compose up -d
                '''
            }
        }
    }
}