from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains



driver = webdriver.Firefox()
driver.get("https://www.tbank.ru/invest/indexes/TIPOUS/")
actions = ActionChains(driver=driver)

try:
    driver.find_element(By.CSS_SELECTOR, 'button[period="year"]').click()

    chart = driver.find_element(By.CLASS_NAME, 'Line__line_MHcc2')
    actions.move_to_element(chart).perform()

finally:
    __import__('time').sleep(3)
    driver.close()

