import requests
import json
from transaction.service import usd_bakai
# from utils.response import Response




"""
https://back.onex.kg/api/v1/account/details = Баланс
https://back.onex.kg/api/v1/orders/status-count = Общее количество полученных товаров и на складах
https://back.onex.kg/api/v1/orders/expected" = Товары которые Ожидаются, так же можно создавать товар(**)
https://back.onex.kg/api/v1/orders?status=at_warehouse = Товары которые на складе в Америке
https://back.onex.kg/api/v1/orders?status=on_the_way = Товары которые в пути
https://back.onex.kg/api/v1/orders/ready-cost = Товары которые готовы на выдачу (Проверить)
"""


url = "https://back.onex.kg/api/v1/orders?status=at_warehouse"
USD_SOM = 1

access_token = "eyJ0eXAiOiJKV1QiLCJhbGciOiJIUzI1NiJ9.eyJpc3MiOiJodHRwczovL2JhY2sub25leC5rZy9hcGkvbG9naW4iLCJpYXQiOjE3MjcxNTMwMjAsImV4cCI6MTc4NzE1Mjk2MCwibmJmIjoxNzI3MTUzMDIwLCJqdGkiOiJIWmJoTVJXWXRKZG55U0dNIiwic3ViIjoiNjYyNCIsInBydiI6IjIzYmQ1Yzg5NDlmNjAwYWRiMzllNzAxYzQwMDg3MmRiN2E1OTc2ZjciLCJ1bmlxdWVfaWQiOiI3NmQ4N2QyMi1kMDU2LTRjYTctOTNjYS1lOTdkYmRiYmQwOTYifQ.nWfKCZOFxJGGWJt3ah9bdaUX8d4Fgc08dJtvq572FBY"

headers = {
    "Authorization": f"Bearer {access_token}",
    "Content-Type": "application/json",
    "Accept-Encoding":"gzip",
    "Accept": "application/json"
}

params = {
    'per_page': 100,  # Количество элементов для получения
}

bakai = usd_bakai()

def at_warehouse():
    response = requests.get('https://back.onex.kg/api/v1/orders?status=at_warehouse', headers=headers)
    data = response.json()

    info = data.get("data")["data"]
    summary = 0
    array = []
    for i in info:
        summary += i.get('cost')
        array.append(f"{i.get('tracking_code')} - {i.get('customer_comment')} - {round(float(i.get('cost')) / bakai * 0.9, 2)} $")
    return 200, json.dumps({"data":array}).encode("utf-8")


def on_the_way():
    response = requests.get('https://back.onex.kg/api/v1/orders?status=on_the_way', headers=headers, params=params)
    data = response.json()

    info = data.get("data")["data"]
    print(len(info))
    summary = 0
    array = []
    for i in info:
        summary += i.get('cost')
        array.append(f"{i.get('tracking_code')} - {i.get('customer_comment')} - {round(float(i.get('cost')) / bakai * 0.9, 2)} $")
    return 200, json.dumps({"data":array}).encode("utf-8")


def ready():
    response = requests.get('https://back.onex.kg/api/v1/orders/ready-cost', headers=headers)
    data = response.json()

    # response_size_kb = len(response.content) / 1024  # в КБ
    info = data.get("data")["data"]
    summary = 0
    array = []
    for i in info:
        summary += i.get('cost')
        array.append(f"{i.get('tracking_code')} - {i.get('customer_comment')} - {round(float(i.get('cost')) / bakai * 0.9, 2)} $")
    return 200, json.dumps({"data":array}).encode("utf-8")
