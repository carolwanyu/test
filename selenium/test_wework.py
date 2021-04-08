import json
import time
from selenium import webdriver


class TestWework:
    def setup(self):
        # 声明 chrome 的参数
        chrome_arg = webdriver.ChromeOptions()
        # 加入调试地址
        chrome_arg.debugger_address = '127.0.0.1:9222'
        self.driver = webdriver.Chrome()
        self.vars = {}

    def teardown(self):
        self.driver.quit()

    def test_login(self):
        self.driver.get("https://work.weixin.qq.com/")
        self.driver.find_element_by_class_name("index_top_operation_loginBtn").click()

    def test_get_cookie(self):
        self.driver.get("https://work.weixin.qq.com/")
        # 获取cookie
        # g_cookie = self.driver.get_cookies()
        # 写入cookie
        # with open("cookie.txt", "w", encoding="utf-8") as f:
        #     json.dump(g_cookie, f)

        # 打开存储cookie的文件，序列化
        with open("cookie.txt", "r", encoding="utf-8") as f:
            cookie = json.load(f)
        # 添加cookie
        for i in cookie:
            self.driver.add_cookie(i)
        self.driver.refresh()
        self.driver.find_element_by_class_name("index_top_operation_loginBtn").click()
        time.sleep(6)




