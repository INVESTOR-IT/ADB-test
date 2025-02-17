from typing import List, Dict
import pymysql

import config  # Файл с секретными дыннами БД


def connection():
    '''Подключение к БД, возвращает Сonnection'''

    try:
        connection = pymysql.connect(
            host=config.host,
            port=3306,
            user=config.user,
            password=config.password,
            database=config.name_database,
            cursorclass=pymysql.cursors.DictCursor
        )
    except Exception as err:
        print(f'Ошибка: {err}')

    return connection


def select(sql: str) -> List[Dict]:
    '''Получение из БД данные'''

    connect = connection()
    try:
        with connect.cursor() as cursor:
            cursor.execute(sql)
            rows = cursor.fetchall()
    finally:
        connect.close()

    return rows


def insert(sql: str) -> None:
    '''Добавление в БД данные'''

    connect = connection()
    try:
        with connect.cursor() as cursor:
            cursor.execute(sql)
            connect.commit()
    finally:
        connect.close()
