pipeline {
    agent any
    
    parameters {
        string(name: 'MY_PARAMETER', defaultValue: 'No value Assingned', description: 'Enter a dynamic value')
    }

    stages {
        stage('Print Parameter Value') {
            steps {
                script {
                    echo "${params.MY_PARAMETER}"
                }
            }
        }
    }
}
