from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains

import db


def parser() -> dict:
    '''Реализация парсера, получение данных с сайта'''

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


def writing_o_db(data: dict) -> None:
    '''Запись значение в БД'''

    values = ', '.join(str((0, key, value)) for key, value in data.items())
    request = f'INSERT INTO Chart (id, point, price) VALUES {values}'
    db.insert(request)


if __name__ == '__main__':
    parser()
    # data = parser() # Данные с сайта {1: 308.35, ...}
    # writing_o_db(data)
