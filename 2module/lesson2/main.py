# python date
import datetime
"""
Основной функционал для работы с датами и временем сосредоточен в модуле datetime в виде следующих классов:
date
datetime

Преобразование из строки в дату
strptime()

Для определения формата мы можем использовать следующие коды:

%d: день месяца в виде числа

%m: порядковый номер месяца

%y: год в виде 2-х чисел

%Y: год в виде 4-х чисел

%H: час в 24-х часовом формате

%M: минута

%S: секунда
"""
#
# currentDay = datetime.datetime.now()
# someDay = datetime.timedelta(5)
# print(currentDay + someDay)

startDay = datetime.datetime.strptime("01.01.2023", "%d.%m.%Y")
currentDay = datetime.datetime.strptime("10.03.2023", "%d.%m.%Y")
# someDay = datetime.date(2000, 10, 7).year

print((currentDay - startDay).days)

day1 = datetime.datetime.now().weekday() # 0 monday
print(day1)



