pipeline {
    agent any
    
    stages {
        stage('Stage 1') {
            steps {
                script {
                    echo "this is sugumar"
                }
            }
        }
        
        stage('Trigger Pipeline 2') {
            steps {
                script {
                    Native= "hosur"
                    build job: 'Pipeline2', parameters: [string(name: 'Value', value: Native)], wait: false
                }
            }
        }
    }
}
