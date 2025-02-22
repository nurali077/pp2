from datetime import datetime

now = datetime.now().replace(microsecond=0)

print("дата сейчас без микросекунды: ", now)
