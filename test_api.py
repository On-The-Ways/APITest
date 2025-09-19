# 示例：API测试代码
import requests
import pytest
import allure

@allure.feature("API测试")
@allure.story("基础接口测试")
def test_api_endpoint():
    response = requests.get("https://yuanbao.tencent.com/chat/naQivTmsDa")
    assert response.status_code == 200

# 添加更多API测试用例
@allure.feature("API测试")
@allure.story("响应结构验证")
def test_api_response_structure():
    response = requests.get("https://yuanbao.tencent.com/chat/naQivTmsDa")
    assert response.status_code == 200
    data = response.json()
    # 验证返回数据的基本结构
    assert "id" in data or "username" in data

@allure.feature("API测试")
@allure.story("异常接口测试")
def test_api_invalid_endpoint():
    # 测试不存在的端点
    response = requests.get("https://yuanbao.tencentabc.com/chat/nonexistent")
    assert response.status_code == 404

if __name__ == "__main__":
    # 可以通过命令行直接运行此文件来执行测试
    # 使用方式: python ApiTest.py
    pytest.main([__file__, "-v", "--alluredir=./allure-results"])