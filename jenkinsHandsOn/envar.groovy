pipeline {
    agent any
    
    environment {
        my_var = 'Hello !, This is sugumar'
    }

    stages {
        stage('Print Environment Variable') {
            steps {
                script {
                    echo " ${env.my_var}"
                }
            }
        }
    }
}
