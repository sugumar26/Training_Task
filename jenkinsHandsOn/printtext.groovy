pipeline {
    agent any
    
    stages {
        stage('Print Message') {
            steps {
                echo 'Hello !!! I am sugumar, from hosur , krishnagiri'
            }
        }
    }
}
