pipeline {
    agent any
    
    tools {
        // 如果您在Jenkins中配置了Python工具，可以在这里指定
        // python "Python3"
    }
    
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
                    // 安装依赖
                    bat 'pip install -r requirements.txt'
                    // 或者直接安装需要的包
                    // bat 'pip install requests pytest allure-pytest selenium'
                }
            }
        }
        
        stage('Run API Tests') {
            steps {
                script {
                    // 运行API测试
                    bat 'python test_api.py'
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
                    bat 'python test_web.py'
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
                    bat 'allure generate allure-results -o allure-report --clean'
                }
            }
        }
    }
    
    post {
        always {
            // 发布Allure报告
            publishHTML([
                allowMissing: false,
                alwaysLinkToLastBuild: true,
                keepAll: true,
                reportDir: 'allure-report',
                reportFiles: 'index.html',
                reportName: 'Allure Report'
            ])
            
            // 或者使用Allure插件（如果已安装）
            // allure([
            //     includeProperties: false,
            //     jdk: '',
            //     properties: [],
            //     reportBuildPolicy: 'ALWAYS',
            //     results: [[path: 'allure-results']]
            // ])
        }
    }
}