numbers = [77,89,50,19,2]

first = float("-inf")
second = float("-inf")

for num in numbers:
    if num > first:
        second = first
        first = num

    elif num > second and num != first:
        second = num
print(second)






