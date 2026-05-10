A = int(input("Введите первое число: "))
B = int(input("Введите второе число: "))

start = A if A % 2 == 0 else A + 1

print(*range(start, B + 1, 2))