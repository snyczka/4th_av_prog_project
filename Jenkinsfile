pipeline {

    agent any

    environment{
        REPO_URL = 'https://github.com/snyczka/adv_prog_4.git'
    }

    tools{
        gradle 'Gradle'
    }

    parameters{
        
    }

    stages{



        stage("Build"){
            
            steps{

                script{
                    git branch: 'Trivia', url: env.REPO_URL
                }
            }
        }
        stage("test"){

            steps{
                sh 'python manager.py'
            }
        }

    }
}