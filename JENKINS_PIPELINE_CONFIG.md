# Jenkins Pipeline 配置说明

## 前置要求

1. Jenkins服务器已安装并运行
2. Jenkins已安装以下插件:
   - Pipeline (通常默认安装)
   - HTML Publisher Plugin (用于发布Allure报告)
   - Allure Jenkins Plugin (可选，用于更好的Allure集成)
3. 服务器上已安装Python环境
4. 服务器上已安装Allure命令行工具

## Jenkins Pipeline 配置步骤

### 1. 创建Pipeline项目
1. 登录Jenkins
2. 点击"新建任务"
3. 输入任务名称 (例如: "MyTestProject")
4. 选择"流水线(Pipeline)"类型
5. 点击"确定"

### 2. 配置Pipeline
在项目的"流水线"部分，可以选择两种方式定义Pipeline:

#### 方式一: Pipeline script from SCM (推荐)
1. 在"定义"下拉菜单中选择"Pipeline script from SCM"
2. 选择SCM类型 (如Git)
3. 配置仓库URL和凭证
4. 指定分支 (如 `*/main` 或 `*/master`)
5. Script Path保持为 `Jenkinsfile` (如果使用默认名称)

#### 方式二: 直接在Jenkins中编写脚本
1. 在"定义"下拉菜单中选择"Pipeline script"
2. 将Jenkinsfile中的内容复制到脚本区域

### 3. 配置触发器 (可选)
- 可以配置定时构建 (如每天凌晨构建)
- 可以配置SCM轮询 (定期检查代码更新)
- 可以配置GitHub webhook集成 (代码推送时自动构建)

### 4. 配置环境变量 (可选)
如果需要，可以在Pipeline中添加环境变量:
```groovy
environment {
    PYTHON_PATH = 'C:\\Python39\\python.exe'
    ALLURE_RESULTS = 'allure-results'
    ALLURE_REPORT = 'allure-report'
}
```

## Jenkinsfile 说明

当前项目中的Jenkinsfile已经包含了以下阶段:

1. **Checkout** - 检出源代码
2. **Setup Environment** - 安装Python依赖
3. **Run API Tests** - 运行API测试
4. **Run Web Tests** - 运行Web测试
5. **Generate Allure Report** - 生成Allure测试报告

## Allure报告查看

构建完成后，可以在Jenkins构建页面找到"Allure Report"链接来查看测试报告。

## 注意事项

1. 确保Jenkins服务器可以访问测试需要的网络资源
2. Web测试需要服务器能够运行浏览器，建议使用无头模式或远程WebDriver
3. 如果使用Windows节点，需要将脚本中的`sh`命令改为`bat`命令
4. 确保Allure命令行工具已添加到系统PATH中