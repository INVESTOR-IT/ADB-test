from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import MoveTargetOutOfBoundsException, NoSuchElementException


import db


def parser() -> dict:
    '''Реализация парсера, получение данных с сайта'''

    driver = webdriver.Firefox()
    driver.get("https://www.tbank.ru/invest/indexes/TIPOUS/")
    driver.set_window_size(1115, 1115)
    actions = ActionChains(driver=driver)
    coordinates = ('217.33333333333337, 38.69999999999999', '173.8666666666667, 38.69999999999999', '130.39999999999998, 167.30422360248485',
                   '86.93333333333331, 84.9171428571428', '43.466666666666654,192.42223602484518', '0,127.28285714285673', '-43.466666666666654,201.63217391304318')

    try:
        driver.find_element(By.CSS_SELECTOR, 'button[period="year"]').click()

        chart = driver.find_element(By.CLASS_NAME, 'Line__line_MHcc2')
        actions.move_to_element(chart).move_by_offset(467.984375, 308.3).click().perform()

        print(driver.find_element(By.CSS_SELECTOR, 'text.PointTooltip__tooltipTextBlack_u10tB[text-anchor="end"]').text)

    except MoveTargetOutOfBoundsException:
        print('Error: координата вне окна')

    except NoSuchElementException:
        print('Eror: Элемент не найден')

    finally:
        __import__('time').sleep(5)
        driver.close()


def writing_o_db(data: dict) -> None:
    '''Запись значение в БД'''

    values = ', '.join(str((0, key, value)) for key, value in data.items())
    request = f'INSERT INTO Chart (id, point, price) VALUES {values}'
    db.insert(request)


if __name__ == '__main__':
    data = parser()  # Данные с сайта {1: 308.35, ...}
    # writing_o_db(data)
