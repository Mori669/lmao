import requests
import numpy as np


# Отправление GET запроса для проверки URL
response = requests.get('https://urban-university.ru/members/courses/course999421818026/20231222-0000domasnee-zadanie-po-teme-obzor-storonnih-bibliotek-python-400269495184')


print(response.status_code)


# Создание массива из списка
arr = np.array([1, 2, 3, 4])

print(arr * 2)
print(arr ** 2)
print((arr + arr)**2)


