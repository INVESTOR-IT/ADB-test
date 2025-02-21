from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import MoveTargetOutOfBoundsException, NoSuchElementException


import db


def parser() -> dict:
    '''Реализация парсера, получение данных с сайта'''

    result = {}

    driver = webdriver.Firefox()
    driver.get("https://www.tbank.ru/invest/indexes/TIPOUS/")
    driver.set_window_size(1115, 1115)
    actions = ActionChains(driver=driver)

    coordinates = ('434.55691964285717,133.98099378882006 '
                   '367.70200892857144,131.6366459627333 '
                   '334.27455357142856,131.6366459627333 '
                   '300.84709821428567,168.97875776397498 '
                   '267.41964285714283,154.21254658385146 '
                   '233.9921875,115.8960248447209 '
                   '200.56473214285717,86.25677018633507 '
                   '167.13727678571433,86.08931677018614 '
                   '133.70982142857144,83.91242236024831').split(' ')
    
    class_point = 'text.PointTooltip__tooltipTextBlack_u10tB[text-anchor="end"]'

    try:
        driver.find_element(By.CSS_SELECTOR, 'button[period="year"]').click()

        result[1] = driver.find_element(By.CLASS_NAME, 'Tooltip__tooltipText_uaadt').text

        chart = driver.find_element(By.CLASS_NAME, 'Indicators__indicatorsText_OntcX')
        __import__('time').sleep(2)  # Задержка что бы все прогрузилось

        for i in range(len(coordinates)):
            x, y = map(float, coordinates[i].split(','))
            actions.move_to_element(chart).move_by_offset(x, y).click().perform()
            result[i + 2] = driver.find_element(By.CSS_SELECTOR, class_point).text

    except MoveTargetOutOfBoundsException:
        print('Error: координата вне окна')

    except NoSuchElementException:
        print('Eror: Элемент не найден')

    finally:
        driver.close()

    return result


def writing_o_db(data: dict) -> None:
    '''Запись значение в БД'''

    values = ', '.join(str((0, key, value)) for key, value in data.items())
    request = f'INSERT INTO Chart (id, point, price) VALUES {values}'
    db.insert(request)


if __name__ == '__main__':
    data = parser()  # Данные с сайта {1: 308.35, ...}
    writing_o_db(data)
