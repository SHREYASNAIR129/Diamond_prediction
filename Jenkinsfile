pipeline{
    agent any

    stages{
        stage("Checkout"){
            steps{
                checkout scmGit(branches: [[name: '*/master']], extensions: [], userRemoteConfigs: [[url: 'https://github.com/SHREYASNAIR129/Diamond_prediction.git']])
            }
        }
        stage("build"){
            steps{
                git 'https://github.com/SHREYASNAIR129/Diamond_prediction.git'
            }
        }
        stage("loading_data"){
            steps{
                bat 'python3 dataLoading.py'
            }
        }
        stage("data_preprocessing"){
            steps{
                sh 'python3 dataPreprocessing.py'
            }
        }
        stage("model_building_and_metrics"){
            steps{
                sh 'python3 modelBuilding.py'
            }
        }
        
    }
    post{
        always{
            emailext body: '', subject: 'This is the new build', to: 'shreyas.jarvis129@gmail.com'
        }
    }
}