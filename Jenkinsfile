pipeline {
    agent any
    environment {
        PROJECT_NAME="Chat_Bot"
    }
    stages {
        stage("Build"){
            steps{
                bat "echo Stage: 1 Build ${env.PROJECT_NAME}"
                bat """
                    python -m venv .venv
                    call .venv\\Scripts\\activate.bat
                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                """
            }
        }
        stage("Test"){
            steps{
                bat "echo Stage: 2 Test ${env.PROJECT_NAME}"
                bat """
                .venv\\Scripts\\python.exe -m pytest
                """
            }
        }
        stage("Deploy"){
            steps{
                bat "echo Stage: 3 Deploy ${env.PROJECT_NAME}"
            }
        }
    }
    post{
        success{
            echo 'Build succeeded!' 
        }
        failure {
            echo 'Build Failed!' 
        }
    }
}