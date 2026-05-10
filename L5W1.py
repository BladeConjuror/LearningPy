num = int(input("Введите целое число: "))

if num == 0:
    print("Это ноль")
else:
    if num > 0:
        type = "Положительное"
    else:
        type = "Отрицательное"
    
    # Определяем чётность
    if num % 2 == 0:
        print(f"{type}, четное число")
    else:
        print(f"{type}, нечетное число")