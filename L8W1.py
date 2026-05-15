n = int(input())

numbers = []
for i in range(n):
    numbers.append(int(input()))

reversed = numbers[::-1]

for num in reversed:
    print(num)
