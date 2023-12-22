import math

print("Letter Histogram")
a = input("Enter word or sentence > ")

word = a.replace(" ", "")

alphabet = []
seen_alphabet = []

for i in word:
    if i.isalpha():
        if i not in seen_alphabet:
            seen_alphabet.append(i)
        alphabet.append(i)

seen_alphabet.sort()
word_dict = {}

for i in alphabet:
    word_dict[i] = alphabet.count(i)

x = max(word_dict.values())

row = [" "] * len(seen_alphabet)
table = [row.copy() for _ in range(x)]

row_index = 0
for i in seen_alphabet:
    col_index = x - 1
    for j in range(0, alphabet.count(i)):
        table[col_index][row_index] = "^"
        col_index -= 1
    row_index += 1

first = 0
for i in range(0, max(word_dict.values())):
    print("\n" * (first != 0) + "0" * (len(str(x)) < 3) + "0" * (len(str(x)) < 2) + str(x) + "|", end=" ")
    for j in range(0, len(row)):
        print(table[i][j], end=" ")

    first += 1
    x -= 1

print("\n>>>> ", end="")
for i in seen_alphabet:
    print(i, end=" ")

avg = 0

for _ in alphabet:
    avg = len(alphabet) / len(seen_alphabet)

z = 0
for _ in word_dict:
    z += (word_dict[_] - avg) ** 2

sd = math.sqrt(z / (len(seen_alphabet) - 1))

print("\nMAX = %.2f, MIN = %.2f, AVG = %.2f, S.D. = %.2f" % (max(word_dict.values()), min(word_dict.values()), avg, sd))
