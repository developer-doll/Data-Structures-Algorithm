#Nested For loop
numbers = [1, 2, 2, 3, 1, 4, 3, 5]
result = []

for num in numbers:
    if num not in result:
        result.append(num)
print(result)



#For loop

def for_duplicate(nums):

    seen = []

    for num in nums:

        if num in seen:
            return True

        seen.append(num)

    return False

print(for_duplicate([1,2,2,3,3,1,4]))
print(for_duplicate([1,2,3,4]))



#Two pointers

def point_duplicate(nums):
    n = len(nums)

    # Step 1: Sort without using built-in sort()
    for i in range(n):
        for j in range(0, n - i - 1):
            if nums[j] > nums[j + 1]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]

    # Step 2: Two pointers
    left = 0
    right = 1

    while right < n:
        if nums[left] == nums[right]:
            return True

        left += 1
        right += 1

    return False


print(point_duplicate([1, 2, 2, 3, 3, 1, 4]))  
print(point_duplicate([1, 2, 3, 4]))           


#Dictionary
def dict_duplicate(nums):
    frequency = {}

    for num in nums:
        frequency[num] = frequency.get(num, 0) + 1

        if frequency[num] > 1:
            return True

    return False

print(dict_duplicate([1, 2, 2, 3, 3, 1, 4])) 
print(dict_duplicate([1, 2, 3, 4]))            

