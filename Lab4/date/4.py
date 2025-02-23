from datetime import datetime

a = input("Введите дату в формате YYYY-MM-DD: ")   
b = input("Введите дату в формате YYYY-MM-DD: ")

date_a = datetime.strptime(a, "%Y-%m-%d")
date_b = datetime.strptime(b, "%Y-%m-%d")

difference = (date_a - date_b).total_seconds()

print("Разница в секундах:", difference)