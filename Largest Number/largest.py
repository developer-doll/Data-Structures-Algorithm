n = [45, 89, 32, 11, 66, 67]

first = float('-inf')

for num in n:
    if num > first:
        first = num

print(first)