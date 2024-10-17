import requests, re
from bs4 import BeautifulSoup
from .metadata import *
from .utils import *


url = "https://app.lifeshop.kg/auth/login"
result = {}

def func():
    for login, password, tokens, cookies_ in zip(LOGIN, PASSWORD, TOKENS, COOKIES_):
        data = {
                    "authenticity_token": tokens,
                    "user[email]": login,
                    "user[password]": password,
                    "commit": "Войти"
                }

        HEADERS['Cookie'] = cookies_

        response = requests.post(url, headers=HEADERS, data=data)
        soup = BeautifulSoup(response.text, 'lxml')
        array = []
        packages_block = soup.find('div', class_='mt-8 border border-gray-200 rounded-md divide-y')
        all_packages = packages_block.find_all('div', class_='relative px-5 py-3 space-y-1')

        """Собирает и фильтрует товары по дате у каждого юзера"""
        for package in all_packages:
            package_status = package.find('div', class_='flex items-center gap-x-1').text.strip()
            data = []
            if package_status in ['Таможенное оформление','В пути']:
                package_text = package.find('div', class_='text-sm text-gray-700').text.strip().replace('\n', '').split('⨯')
                if not is_date_within_2_weeks(package_text[0].split()[-1]):
                    package_track = package.find('div', class_='font-semibold text-gray-900 w-56 md:w-auto truncate').text.strip()
                    #TODO
                    """"Дописать добавление товара в черный список"""
                else:
                    package_track = package.find('div', class_='font-semibold text-gray-900 w-56 md:w-auto truncate').text.strip()
                    package_weight = float(re.sub(r'[^\d.]', '',package.find('div', class_='w-fit rounded-full px-2 text-sm font-medium bg-lime-100 text-lime-600').text.strip()))*12
                    data += package_text, round(package_weight, 2), package_status, package_track
                    array.append(data)
                
        if len(array) >= 1:
            if login not in result:
                result[login]=array
    return result

print(func())