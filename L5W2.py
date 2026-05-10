word = input("Введите слово из маленьких латинских букв: ")

vowels = "aeiou"
counts = {'a': 0, 'e': 0, 'i': 0, 'o': 0, 'u': 0}
vowel_total = 0
consonant_total = 0

for i in word:
    if i in vowels:
        vowel_total += 1
        counts[i] += 1
    else:
        consonant_total += 1

print("Количество гласных букв:", vowel_total)
print("Количество согласных букв:", consonant_total)

for v in vowels:
    print(f"Количество букв '{v}':", counts[v] if counts[v] > 0 else False)