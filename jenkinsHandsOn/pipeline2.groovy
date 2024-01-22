pipeline {
    agent any
    
    parameters {
        string(name: 'Value', defaultValue: '', description: 'Value from Pipeline1')
    }
    
    stages {
        stage('Pipeline 2 Stage 1') {
            steps {
                script {
                    echo "I am from  ${params.Value}"
                }
            }
        }
    }
}
