from selenium import webdriver
from selenium.webdriver.common.by import By

driver = webdriver.Firefox()
driver.get("https://www.tbank.ru/invest/indexes/TIPOUS/")


try:
    driver.find_element(By.CSS_SELECTOR, 'button[period="year"]').click()


finally:
    __import__('time').sleep(3)
    driver.close()
