pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Repository checked out successfully.'
            }
        }

        stage('Verify Python') {
            steps {
                sh 'python3 --version'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }
        }

        stage('Run Tests') {
            steps {
                sh 'python3 test_app.py'
            }
        }

        stage('Build Complete') {
            steps {
                echo 'Application Build Successful!'
            }
        }
    }

    post {
        success {
            echo 'Pipeline completed successfully!'
        }

        failure {
            echo 'Pipeline failed!'
        }
    }
}