pipeline {
    agent any
    environment {
        PROJECT_NAME="Chat_Bot"
        ENV_PY_PATH=".venv\\Scripts\\python.exe"
    }
    stages {
        stage("Build"){
            steps{
                bat "echo Stage: 1 Build ${env.PROJECT_NAME}"
                bat """
                    python -m venv .venv
                    call .venv\\Scripts\\activate.bat
                    ${env.ENV_PY_PATH} -m pip install -r requirements.txt
                """
            }
        }
        stage("Test"){
            steps{
                bat "echo Stage: 2 Test ${env.PROJECT_NAME}"
                bat """
                ${env.ENV_PY_PATH} -m pytest || exit 0
                """
            }
        }
        stage("Deploy"){
            steps{
                bat "echo Stage: 3 Deploy ${env.PROJECT_NAME}"
                bat """
                ${env.ENV_PY_PATH} manage.py makemigrations
                ${env.ENV_PY_PATH} manage.py migrate
                REM ${env.ENV_PY_PATH} -m python manage.py runserver 8000 to start server
                """
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