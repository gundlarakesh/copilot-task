pipeline {
    agent any
    enviroment {
        PROJECT_NAME="Chat_Bot"
    }
    stages {
        stage("Build"){
            steps{
                bat "echo Stage: 1 Build"
            }
        }
        stage("Test"){
            steps{
                bat "echo Stage: 2 Test ${env.PROJECT_NAME}"
            }
        }
        stage("Deploy"){
            steps{
                bat "echo Stage: 3 Deploy"
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