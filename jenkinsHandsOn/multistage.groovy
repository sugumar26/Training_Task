pipeline {
    agent any
    
    stages {
        stage('create_dir') {
            steps {
                script {
                    bat 'if not exist sugumar_dir mkdir sugumar_dir'
                }
            }
        }
        
        stage('Add_file') {
            steps {
                script {
                    bat 'echo "This is a file" > sugumar_dir/file.txt'
                }
            }
        }
        
        stage('add_content') {
            steps {
                script {
                    bat 'echo "append" >> sugumar_dir/file.txt'
                }
            }
        }
        
        stage('display') {
            steps {
                script {
                    bat 'if exist sugumar_dir\\file.txt (Type sugumar_dir\\file.txt) else (echo "File not found")'
                }
            }
        }
    }
}
