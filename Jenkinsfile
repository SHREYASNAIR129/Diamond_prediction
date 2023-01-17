pipeline{
    agent any

    stages{
        stage("Checkout"){
            steps{
                checkout([$class: 'GitSCM', branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/SHREYASNAIR129/Diamond_prediction.git']]])
            }
        }
        stage("build"){
            steps{
                git 'https://github.com/SHREYASNAIR129/Diamond_prediction.git'
                bat label: '', script: 'python3 dataLoading.py'
            }
        }
    }
}