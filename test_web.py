# 示例：使用Selenium进行网页测试
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.chrome.options import Options
import pytest
import time
import allure

@pytest.fixture
def driver():
    chrome_options = Options()
    # 启用无头模式，适用于Jenkins等无GUI环境
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--window-size=1920,1080")
    
    driver = webdriver.Chrome(options=chrome_options)
    yield driver
    driver.quit()

@allure.feature("Web测试")
@allure.story("登录功能测试")
def test_login(driver):
    driver.get("https://uniportal.huawei.com/uniportal1/login-pc.html?redirect=https%3A%2F%2Fcareer.huawei.com%2Freccampportal%2Flogin_index.html%3Fredirect%3Dhttps%3A%2F%2Fcareer.huawei.com%2Freccampportal%2Fportal5%2Fcampus-recruitment.html%3Fsessionid%3D%3Fi%3D10370#/passwordLogin")
    
    # 等待页面元素加载
    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "username"))
    )
    
    driver.find_element(By.ID, "username").send_keys("13330194845")
    driver.find_element(By.ID, "password").send_keys("zxcvbnm.123")
    driver.find_element(By.ID, "login-btn").click()
    
    # 等待页面跳转并验证
    time.sleep(3)
    assert "job-progress" in driver.current_url or "campus-recruitment" in driver.current_url

# 添加测试页面元素存在的用例
@allure.feature("Web测试")
@allure.story("页面元素验证")
def test_login_page_elements(driver):
    driver.get("https://uniportal.huawei.com/uniportal1/login-pc.html?redirect=https%3A%2F%2Fcareer.huawei.com%2Freccampportal%2Flogin_index.html%3Fredirect%3Dhttps%3A%2F%2Fcareer.huawei.com%2Freccampportal%2Fportal5%2Fcampus-recruitment.html%3Fsessionid%3D%3Fi%3D10370#/passwordLogin")
    
    # 验证关键元素存在
    assert driver.find_element(By.ID, "username") is not None
    assert driver.find_element(By.ID, "password") is not None
    assert driver.find_element(By.ID, "login-btn") is not None

if __name__ == "__main__":
    # 可以通过命令行直接运行此文件来执行测试
    # 使用方式: python WebTest.py
    pytest.main([__file__, "-v", "--setup-show", "--alluredir=./allure-results"])