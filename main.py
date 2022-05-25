from fast_bitrix24 import Bitrix
import datetime
import holidays
import schedule

webhook = "https://b24-uxw5nw.bitrix24.ru/rest/1/jxcujeqn73soik0d/"
b = Bitrix(webhook)

# Словарь праздников
ru_holidays = holidays.RU()

today = datetime.date.today()
day_plus_3 = today + datetime.timedelta(days=3)
check_holiday = today + datetime.timedelta(days=3) in ru_holidays

ru_holidays_name = ru_holidays.get(day_plus_3)


def task_holiday(today_check, day, name):
    if today_check == True:
        task = {"ID": 1, 'fields': {"TITLE": f"{day} будет {name}!\n"
                                             f"Не забудь поздравить всех причастных)", 'RESPONSIBLE_ID': '1'}}
        b.call('tasks.task.add', task)
    else:
        print('Через 3 дня нет праздников\n'
              'Засыпаю до завтра')

schedule.every().day.at('10:00').do(task_holiday, check_holiday, day_plus_3, ru_holidays_name)
while True:
    schedule.run_pending()
