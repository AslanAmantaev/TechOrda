def polin(s):
    a=""
    s=s.replace(" ","").lower()
    for i in s:
        a=i+a
    return a
s=str(input("Введите строку: "))
s=s.replace(" ","").lower()
if s==polin(s):
    print("-строка Палиндром")
else:
    print("- строка НЕ Полиндром")
