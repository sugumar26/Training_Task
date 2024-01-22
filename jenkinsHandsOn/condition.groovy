pipeline {
    agent any

    stages {
        stage('Stage 1') {
            when {
                expression { return true } 
            }
            steps {
                echo 'Running Stage 1'
            }
        }

        stage('Stage 2') {
            when {
                expression { return false }
            }
            steps {
                echo 'Running Stage 2'
            }
        }

        stage('Stage 3') {
            when {
                expression { return true } 
            }
            steps {
                echo 'Running Stage 3'
            }
        }
    }
}
