n = int(input())

arr = list(map(int, input().split()))

result = []
left = 0
right = n - 1

for i in range(n):
    if i % 2 == 0:
        result.append(arr[right])
        right -= 1
    else:
        result.append(arr[left])
        left += 1

print(result)
