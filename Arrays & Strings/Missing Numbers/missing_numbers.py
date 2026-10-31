#Using sum inbuilt function

def missing_number(nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = sum(nums)

    return expected_sum - actual_sum

print(missing_number([3,0,1]))


#Using for loop

def missing_number(nums):
    n = len(nums)

    expected_sum = n * (n + 1) // 2
    actual_sum = 0

    for num in nums:
        actual_sum += num

    return expected_sum - actual_sum

print(missing_number([2,1,4,0]))



#Nested for loop

def find_disappeared_numbers(nums):
    n = len(nums)
    missing = []

    for num in range(1, n + 1):
        found = False

        for value in nums:
            if value == num:
                found = True
                break

        if not found:
            missing.append(num)

    return missing


print(find_disappeared_numbers([4, 3, 2, 7, 8, 2, 3, 1]))