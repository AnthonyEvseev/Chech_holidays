from fast_bitrix24 import Bitrix

# webhook = "https://b24-uxw5nw.bitrix24.ru/rest/1/jxcujeqn73soik0d/"
# b = Bitrix(webhook)
# deals = b.get_all('tasks.task.list')

# task = {"ID": 1, 'fields': {"TITLE": 'task for test', 'RESPONSIBLE_ID': '1'}}
# leads = b.call('tasks.task.add', task)

from datetime import date
import holidays

ru_holidays = holidays.RU() # this is a dict

a = date(2022, 7, 1) in ru_holidays # True
b = date(2022, 1, 2) in ru_holidays # False
c = ru_holidays.get('2014-01-01')
d = ru_holidays.keys[1]




print(f' Скоро {ru_holidays[2]}! Не забудь позравить всех причастных к празднику)')
#print(f'{ru_holidays.keys()}')
print(d)