from utils.webdriver_manager import WebDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys

class FindJobs:
    def __init__(self, url: str, driver_manager: WebDriverManager):
        self.driver: WebDriver = driver_manager.get_driver()
        self.url = url

    def accept_cookies(self):
        self.driver.find_element(By.ID, "didomi-notice-agree-button").click()

    def ignore_google_login(self):
        try:
            self.driver.find_element(By.XPATH, '//*[@id="loginForm"]/div[1]/div/div[2]/a')
            return True
        except:
            return False
                
    def login(self, email: str, password: str):
        self.driver.get(self.url)
        self.accept_cookies()
        self.driver.find_element(By.ID, "Email").send_keys(email)        
        self.driver.find_element(By.CLASS_NAME, "js_loginButton").click()
        sleep(1)
        if self.ignore_google_login():
            self.driver.find_element(By.CLASS_NAME, "js_loginButton").click()
            self.driver.find_element(By.ID, "Password").send_keys(password)
            self.driver.find_element(By.CLASS_NAME, "js_loginButton").click()
