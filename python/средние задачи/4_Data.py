from datetime import datetime

def res(a):
    try:
        datetime.strptime(a, "%d.%m.%Y")
        return True
    except ValueError:
        return False

b=input("Введите дату:")
if res(b):
    print(b,"Дата корректна")
else:
    print(b, "Дата НЕкорректна")