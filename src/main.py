from utils.webdriver_manager import WebDriverManager
from scrapers.find_jobs import FindJobs
from dotenv import load_dotenv
import os

load_dotenv()

email = os.getenv("EMAIL")
password = os.getenv("PASSWORD")


web_driver_manager = WebDriverManager()
find_jobs = FindJobs("https://login.infojobs.com.br/Account/Login", web_driver_manager)
find_jobs.login(email, password)
find_jobs.search_jobs("desenvolvedor")