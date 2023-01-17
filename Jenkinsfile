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
                git branch: 'master', url: 'https://github.com/SHREYASNAIR129/Diamond_prediction.git'
            }
        }
        stage("loading_data"){
            steps{
                cmd 'python3 dataLoading.py'
            }
        }
        stage("data_preprocessing"){
            steps{
                cmd 'python3 dataPreprocessing.py'
            }
        }
        stage("model_building_and_metrics"){
            steps{
                cmd 'python3 modelBuilding.py'
            }
        }
    }
}