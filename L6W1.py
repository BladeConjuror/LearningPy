N = int(input("Введите количество чисел: "))

zero_count = 0

for i in range(N):
    num = int(input("Введите число: "))
    if num == 0:
        zero_count += 1

print("Количество нулей:", zero_count)