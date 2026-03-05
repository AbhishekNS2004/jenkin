pipeline {
    agent any

    stages {

        stage('Clone Repository') {
            steps {
                git branch: 'main', url: 'https://github.com/AbhishekNS2004/jenkin.git'
            }
        }

        stage('Install Dependencies') {
            steps {
                sh '''
python3 -m venv venv
. venv/bin/activate
pip install -r requirements.txt
'''
            }
        }

        stage('Run Tests') {
            steps {
                sh '''
. venv/bin/activate
pytest
'''
            }
        }

        stage('Run Application') {
            steps {
                sh '''
. venv/bin/activate
python3 app.py
'''
            }
        }
    }
}