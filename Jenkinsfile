pipeline {
    agent { label 'esimtest_pipeline' } // Ensure this label matches your Jenkins node configuration

    stages {
        stage('Start') {
            steps {
                echo 'Pipeline execution started on the specific node!'
            }
        }
        stage('Pull Repository') {
            steps {
                // Clone the Git repository
                git branch: 'cicd_test', url: 'https://github.com/Simtestlab/test_repo.git'
            }
        }
        stage('Install Dependencies') {
            steps {
                // Install required Python packages
                bat 'pip install -r requirements.txt' // Use 'pip3' if needed
            }
        }
        stage('Run Tests') {
            steps {
                // Execute pytest and generate a JUnit XML report
                bat 'pytest --junitxml=results.xml'
            }
        }
    }
    post {
        always {
            // Publish test results to Jenkins
            junit 'results.xml'
        }
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
