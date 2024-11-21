import requests
from bs4 import BeautifulSoup


def best_rub_bank():
    response = requests.get("https://valuta.kg/")
    soup = BeautifulSoup(response.text, 'lxml')

    rows = soup.find_all('tr')
    banks_info = soup.find_all('div', class_='td-member__info')

    currency_arr=[]
    bank_array=[]
    # Цикл по каждому банку
    for bank_info in banks_info:
        bank_link = bank_info.find('a')
        
        if bank_link:
            bank_name = bank_link.text  # Название банка
            bank_array.append(bank_name)

            
    # Перебираем строки и вытаскиваем данные
    for row in rows:
        currency = row.find('div', class_='rate-name')
        if currency and 'rub' in currency.text:
            rates = row.find_all('div', class_='rate -md')
            if rates:
                buy_rate = rates[0].text  # Курс покупки
                currency_arr.append(buy_rate)


    bank_rates = list(zip(bank_array, map(float, currency_arr)))
    best_bank, best_rate = min(bank_rates, key=lambda x: x[1])
    # return (f"Банк с самым лучшим курсом: {best_bank}, Курс: {best_rate}")
    return best_rate


def usd_bakai():
    response = requests.get("https://bakai24.bakai.kg/v1/currency_rates").json()

    usd = response.get('currencies')[0]

    sell_price = usd.get('sell')

    return sell_price


def transfer(amount):
    res = int(amount) * float(best_rub_bank()) / usd_bakai()
    return f"Вы получите: {round(res, 2)}$\nКурс рубля: {best_rub_bank()}"
