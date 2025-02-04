# Импортируем модуль configuration, который, мы создали выше - он содержит настройки подключения и путь к документации
import configuration

# Импортируем модуль requests, который предназначен для отправки HTTP-запросов
# Это популярная библиотека, которая позволяет взаимодействовать с веб-сервисами
import requests

# Импорт данных запроса из модуля data, в котором определены заголовки и тело запроса
import data 

def post_new_orders(body):
    return requests.post(configuration.URL_SERVICE + configuration.CREATE_orders,
                        json=body,
                        headers=data.headers) 


def get_order_by_track(track):
    print(track)
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_track,
                        params={"t":track})
