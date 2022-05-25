from fast_bitrix24 import Bitrix
from datetime import date
import holidays

ru_holidays = holidays.RU()  # this is a dict

a = date(2022, 7, 1) in ru_holidays  # Я не могу удалить эту строчку =D Перестаёт работать код и я ПОКА не понял почему

ru_holidays_name = list(ru_holidays.values())
ru_holidays_data = list(ru_holidays.keys())


for item_name, item_data in zip(ru_holidays_name, ru_holidays_data):
    webhook = "https://b24-uxw5nw.bitrix24.ru/rest/1/jxcujeqn73soik0d/"
    b = Bitrix(webhook)
    deals = b.get_all('tasks.task.list')
    task = {"ID": 1, 'fields': {"TITLE": f"{item_data} будет {item_name}", 'RESPONSIBLE_ID': '1'}}
    leads = b.call('tasks.task.add', task)
