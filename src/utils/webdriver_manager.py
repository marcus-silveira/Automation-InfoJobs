from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


class WebDriverManager:
    def __init__(self, incognito=False):
        self.chrome_options = Options()
        self.service = Service(ChromeDriverManager().install())

        if incognito:
            self.chrome_options.add_argument('--incognito')
            
        self.chrome_options.add_argument('--start-maximized')
        self.driver = webdriver.Chrome(options=self.chrome_options, service=self.service)

    def get_driver(self):
        return self.driver

    def close_driver(self):
        self.driver.quit()
