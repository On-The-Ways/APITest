pipeline {
    agent any
    
    environment {
        // 定义环境变量
        ALLURE_RESULTS = "allure-results"
        ALLURE_REPORT = "allure-report"
    }
    
    stages {
        stage('Checkout') {
            steps {
                // 检出代码
                checkout scm
            }
        }
        
        stage('Setup Environment') {
            steps {
                script {
                    // 检查Python和pip是否可用
                    sh 'which python || which python3'
                    sh 'which pip || which pip3 || python -m ensurepip || python3 -m ensurepip'
                    
                    // 升级pip并安装依赖
                    sh 'python -m pip install --upgrade pip || python3 -m pip install --upgrade pip'
                    sh 'pip install -r requirements.txt || pip3 install -r requirements.txt'
                }
            }
        }
        
        stage('Run API Tests') {
            steps {
                script {
                    // 运行API测试
                    sh 'python test_api.py || python3 test_api.py'
                }
            }
            post {
                always {
                    // 即使测试失败也要继续
                    echo 'API tests completed'
                }
            }
        }
        
        stage('Run Web Tests') {
            steps {
                script {
                    // 运行Web测试
                    sh 'python test_web.py || python3 test_web.py'
                }
            }
            post {
                always {
                    echo 'Web tests completed'
                }
            }
        }
        
        stage('Generate Allure Report') {
            steps {
                script {
                    // 生成Allure报告
                    sh 'allure generate allure-results -o allure-report --clean'
                }
            }
        }
    }
    
    post {
        always {
            // 使用archiveArtifacts而不是publishHTML来存档报告
            archiveArtifacts artifacts: 'allure-report/**', allowEmptyArchive: true
            
            // 如果安装了HTML Publisher插件，可以取消注释下面的代码
            // publishHTML([
            //     allowMissing: false,
            //     alwaysLinkToLastBuild: true,
            //     keepAll: true,
            //     reportDir: 'allure-report',
            //     reportFiles: 'index.html',
            //     reportName: 'Allure Report'
            // ])
        }
    }
}