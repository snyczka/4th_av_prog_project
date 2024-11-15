pipeline {

    agent any

    environment{
        REPO_URL = 'https://github.com/snyczka/adv_prog_4.git'
    }

    tools{
        gradle
    }

    parameters{
        
    }

    stages{



        stage("Trivia"){
            
            steps{
                
                git branch: 'Trivia', url: env.REPO_URL
                cd 'Project/src'
                sh 'python3 manager.py'
                sh ''
            
            }
        }
        stage("ECommerce"){

            steps{
                
                git branch: 'Ecomerce', url: env.REPO_URL
                cd 'obligatorio_2/app/src/main'
                sh ''
                sh ''

            }
        }
        stage("USQL"){

            steps{
                git branch: 'USQL', url: env.REPO_URL
                cd 'USQL'
                sh 'python3 __init__.py'
                sh 'python3 '

            }
        }
    }
}
