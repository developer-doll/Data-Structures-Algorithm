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