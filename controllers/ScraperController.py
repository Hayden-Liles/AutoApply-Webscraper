from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver import ActionChains
import time

class ScraperController:
    def __init__(self):
        self.driver = webdriver.Chrome()
        self.actions = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def contains_email(self, tag):
        if tag.name != 'input':
            return False
        if 'email' in tag.get_text().lower():
            return True
        for attr in tag.attrs.values():
            if isinstance(attr, str) and 'email' in attr.lower():
                return True
        return False
    
    def contains_password(self, tag):
        if tag.name != 'input':
            return False
        if 'password' in tag.get_text().lower():
            return True
        for attr in tag.attrs.values():
            if isinstance(attr, str) and 'password' in attr.lower():
                return True
        return False
    
    def contains_signIn(self, tag):
        if tag.name != 'button' or 'div':
            return False
        if 'sign in' or 'signin' in tag.get_text().lower():
            return True
        for attr in tag.attrs.values():
            if isinstance(attr, str) and 'sign in' or 'signin' in attr.lower():
                return True
        return False

    def test(self):
        self.driver.get('https://bah.wd1.myworkdayjobs.com/en-US/BAH_Jobs/login')
        time.sleep(5)  # Let the page load for a while as the site has some JS scripts running 

        soup = BeautifulSoup(self.driver.page_source, 'html.parser')
        email_elements = soup.find_all(self.contains_email)
        password_elements = soup.find_all(self.contains_password)
        signIn_elements = soup.find_all(self.contains_signIn)

        for element in email_elements:
            print(element)

        for element in password_elements:
            print(str(element))

        for element in signIn_elements:
            print(str(element))

scraperController = ScraperController()