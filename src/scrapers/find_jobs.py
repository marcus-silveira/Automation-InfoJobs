from utils.webdriver_manager import WebDriverManager
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from time import sleep
from selenium.webdriver.common.keys import Keys


class FindJobs:
    def __init__(self, url: str, driver_manager: WebDriverManager):
        self.driver: WebDriver = driver_manager.get_driver()
        self.url = url
        self.total_pages = None

    def accept_cookies(self):
        self.driver.find_element(By.ID, "didomi-notice-agree-button").click()

    def ignore_google_login(self):
        try:
            self.driver.find_element(
                By.XPATH, '//*[@id="loginForm"]/div[1]/div/div[2]/a')
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

    def search_jobs(self, keyword: str):
        self.driver.get("https://www.infojobs.com.br/")
        self.driver.find_element(
            By.XPATH, '//*[@id="keywordsCombo"]').send_keys(keyword)
        sleep(1)

        self.driver.find_element(By.XPATH, '//*[@id="city"]').click()
        self.driver.find_element(By.XPATH, '//*[@id="city"]').click()
        sleep(1)
        self.driver.find_element(By.XPATH, '//*[@id="city"]').clear()
        self.driver.find_element(
            By.XPATH, '/html/body/main/div[1]/section/div[1]/div[4]/a').click()

        self.total_pages = int(self.driver.find_element(
            By.XPATH, '//*[@id="resumeVacancies"]/div/div[2]').text.split(" ")[-1])

    def apply_jobs(self, keyword: str, home_office: bool = False):
        self.search_jobs(keyword)
        for page in range(1, self.total_pages):
            if home_office:
                self.driver.get(f"https://www.infojobs.com.br/vagas-de-emprego-{keyword}-home_office.aspx?page={page}")

            self.driver.get(f"https://www.infojobs.com.br/vagas-de-emprego-{keyword}.aspx?page={page}")
            jobs = self.driver.find_elements(By.CSS_SELECTOR, "[class='card card-shadow card-shadow-hover text-break mb-16 grid-row js_rowCard ']")
            self.driver.find_element(By.LINK_TEXT, "CANDIDATAR-ME").click()
            for job in jobs:
                job.click()
                sleep(1)
                self.driver.find_element(By.LINK_TEXT, "CANDIDATAR-ME").click()
                sleep(1)
