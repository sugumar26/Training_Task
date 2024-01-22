pipeline {
    agent any
    triggers {
        cron('H * * * *')
    }
    
    stages {
        stage('Run at every hour') {
            steps {
                script {
                    echo 'hello, every hour'
                }
            }
        }
    }
}
