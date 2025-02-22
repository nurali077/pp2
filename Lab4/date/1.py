from datetime import datetime, timedelta

now = datetime.now()

new_date = now - timedelta(days=5)

print("дата сейчас: ", now.strftime("%Y-%m-%d"))

print("дата 5 дней назад: ", new_date.strftime("%Y-%m-%d")) 