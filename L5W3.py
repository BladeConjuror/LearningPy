StartUp = int(input("Минимальная сумма инвестиций: "))
Mike = int(input("Капитал Майкла: "))
Ivan = int(input("Капитал Ивана: "))

if Mike >= StartUp and Ivan >= StartUp:
    print(2)
elif Mike >= StartUp and Ivan < StartUp:
    print("Mike")
elif Mike < StartUp and Ivan >= StartUp:
    print("Ivan")
elif Mike + Ivan >= StartUp:
    print(1)
else:
    print(0)