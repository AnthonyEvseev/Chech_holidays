from fast_bitrix24 import Bitrix
from datetime import date
import holidays
import schedule

ru_holidays = holidays.RU()

a = date(2022, 7, 1) in ru_holidays

ru_holidays_name = list(ru_holidays.values())
ru_holidays_data = list(ru_holidays.keys())

webhook = "https://b24-uxw5nw.bitrix24.ru/rest/1/jxcujeqn73soik0d/"
b = Bitrix(webhook)


def append_task(name, data):
    for item_name, item_data in zip(name, data):
        task = {"ID": 1, 'fields': {"TITLE": f"{item_data} будет {item_name}", 'RESPONSIBLE_ID': '1'}}
        b.call('tasks.task.add', task)


append_task(ru_holidays_name, ru_holidays_data)


def main():
    schedule.every()

# for item_name, item_data in zip(ru_holidays_name, ru_holidays_data):
#     webhook = "https://b24-uxw5nw.bitrix24.ru/rest/1/jxcujeqn73soik0d/"
#     b = Bitrix(webhook)
#     task = {"ID": 1, 'fields': {"TITLE": f"{item_data} будет {item_name}", 'RESPONSIBLE_ID': '1'}}
#     leads = b.call('tasks.task.add', task)
