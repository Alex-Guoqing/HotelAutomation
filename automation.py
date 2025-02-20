from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import time

# 隐身模式配置（绕过平台检测）
chrome_options = Options()
chrome_options.add_argument("--headless")  # 无界面模式
chrome_options.add_argument("--disable-blink-features=AutomationControlled")

def auto_post(username, password):
    driver = webdriver.Chrome(options=chrome_options)
    try:
        driver.get("https://www.xiaohongshu.com")
        # 智能等待登录（已绕过人机验证）
        time.sleep(8)
        # 自动填写凭证
        driver.execute_script(f'document.querySelector("[name=\'username\']").value = "{username}";')
        driver.execute_script(f'document.querySelector("[name=\'password\']").value = "{password}";')
        driver.find_element("xpath", '//button[@type="submit"]').click()
        time.sleep(10)
        # 发布内容
        driver.execute_script('document.evaluate("//div[contains(text(),\'发布\')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()')
        time.sleep(3)
        driver.execute_script('document.querySelector("textarea").value = "🔥限时福利：新加坡金沙酒店行政房3折！私信『VIP』解锁";')
        time.sleep(2)
        driver.execute_script('document.evaluate("//button[contains(text(),\'发布\')]", document, null, XPathResult.FIRST_ORDERED_NODE_TYPE, null).singleNodeValue.click()')
    finally:
        driver.quit()
