from isdayoff import ProdCalendar, DateType
from datetime import date
import asyncio
from fast_bitrix24 import Bitrix

calendar = ProdCalendar(locale='ru')


async def main():
    res = await calendar.month(date(2022, 5, 1), pre=True, locale='ru')
    count = len([DateType.NOT_WORKING for day in res if res[day] == DateType.NOT_WORKING])
    print(f'Days off in a month ', count)


webhook = "https://b24-uxw5nw.bitrix24.ru/rest/1/jxcujeqn73soik0d/"
b = Bitrix(webhook)
deals = b.get_all('tasks.task.list')

#task = {"ID": 1, 'fields': {"TITLE": 'task for test', 'RESPONSIBLE_ID': '1'}}
#leads = b.call('tasks.task.add', task)

loop = asyncio.get_event_loop()
loop.create_task(main())
loop.run_forever()
