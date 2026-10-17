n = [45, 89, 32, 11, 66, 67]

first = float('-inf')
second = float('-inf')
third = float('-inf')

for num in n:
    if num > first:
        third = second
        second = first
        first = num

    elif num > second and num != first:
        third = second
        second = num

    elif num > third and num != second and num != first:
        third = num

print(third)