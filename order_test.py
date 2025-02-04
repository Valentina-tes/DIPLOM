import sender_stand_request
import data


def test_create_order():
    # Создаем заказ
    response = sender_stand_request.post_new_orders(data.body)
    # Сохраняем номер заказа
    track = response.json()["track"]
    # Получаем заказ по номеру
    response_order = sender_stand_request.get_order_by_track(track)
    # Проверяем код ответа
    assert response_order.status_code == 200
