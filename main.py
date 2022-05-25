from environs import Env
from fast_bitrix24 import Bitrix
import datetime
import holidays
import schedule

env = Env()
env.read_env()

WEBHOOK = env.str('WEBHOOK')
b = Bitrix(WEBHOOK)

# Словарь праздников
ru_holidays = holidays.RU()

today = datetime.date.today()
day_plus_3 = today + datetime.timedelta(days=3)
check_holiday = today + datetime.timedelta(days=3) in ru_holidays

holidays_name = ru_holidays.get(day_plus_3)


def task_holiday(today_check, day, name):
    if today_check==False:
        task = {"ID": 1, 'fields': {"TITLE": f"{day} будет {name}!\n"
                                             f"Не забудь поздравить всех причастных)", 'RESPONSIBLE_ID': '1'}}
        b.call('tasks.task.add', task)
    else:
        print('Через 3 дня нет праздников\n'
              'Засыпаю до завтра')


def main(today_check, day, name):
    schedule.every(4).seconds.do(task_holiday, today_check, day, name)
    # schedule.every().day.at('10:00').do(task_holiday, today_check, day, name)
    while True:
        schedule.run_pending()


if __name__ == '__main__':
    main(check_holiday, day_plus_3, holidays_name)