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
                bat label: '', script: 'python dataLoading.py'
            }
        }
        stage("data_preprocessing"){
            steps{
                bat label: '', script: 'python dataPreprocessing.py'
            }
        }
        stage("model_building_and_metrics"){
            steps{
                bat label: '', script: 'python modelBuilding.py'
            }
        }
        
    }
    post{
        always{
            emailext body: '', subject: 'This is the new build', to: 'shreyas.jarvis129@gmail.com'
        }
    }
}