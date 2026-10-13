numbers = [77,89,50,19,2]

first = numbers[0]
second = numbers[0]
third = numbers[0]

for num in numbers:
    if num > first:
        third = second
        second = first
        first = num

    elif num > second and num != first:
        second = num

    elif num > third and num != second:
        third = num

print(third)




