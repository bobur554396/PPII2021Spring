from datetime import datetime

a = datetime.now()
# print(a.year)
# print(a.month)
# print(a.day)
# print(a.hour)
# print(a.minute)
# print(a.second)
# print(a.microsecond)

b = datetime(2021, 2, 16)
print(b)

print(a.strftime('%d/%m/%Y %H:%M:%S'))
