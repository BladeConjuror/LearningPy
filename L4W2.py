num = int(input("Введите пятизначное целое число: "))

units = num % 10             
tens = (num // 10) % 10         
hundreds = (num // 100) % 10       
thousands = (num // 1000) % 10
tens_of_thousands = num // 10000

step1 = tens ** units
step2 = step1 * hundreds
step3 = tens_of_thousands - thousands
result = step2 / step3

print(result)