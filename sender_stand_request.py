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
# Вызов функции post_new_orders с телом запроса для создания нового заказа из модуля data
# response = post_new_orders(data.body)

# response_track = response.json()["track"]

# Вывод HTTP-статус кода ответа на запрос
# Код состояния указывает на результат обработки запроса сервером
# print(response.status_code)

# Функция response.json() позволяет получить тело ответа в формате JSON.
# Это полезно для извлечения данных, полученных в результате запроса, 
# особенно когда сервер возвращает полезные данные в формате JSON.
# Здесь мы вызываем эту функцию и выводим полученный JSON в консоль для наглядности.
# print(response.json()) 

def get_order_by_track(track):
    print(track)
    return requests.get(configuration.URL_SERVICE + configuration.ORDERS_track,
                        params={"t":track})
# response_order = get_order_by_track(response_track)

# print(response_order.json())s