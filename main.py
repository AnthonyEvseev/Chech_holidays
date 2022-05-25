from fast_bitrix24 import Bitrix

# webhook = "https://b24-uxw5nw.bitrix24.ru/rest/1/jxcujeqn73soik0d/"
# b = Bitrix(webhook)
# deals = b.get_all('tasks.task.list')

# task = {"ID": 1, 'fields': {"TITLE": 'task for test', 'RESPONSIBLE_ID': '1'}}
# leads = b.call('tasks.task.add', task)

from datetime import date
import holidays

ru_holidays = holidays.RU()  # this is a dict

a = date(2022, 7, 1) in ru_holidays  # True
b = date(2022, 1, 2) in ru_holidays  # False
ru_holidays_name = list(ru_holidays.values())
ru_holidays_data = list(ru_holidays.keys())

print(ru_holidays_name[10])
print(ru_holidays_data[10])
