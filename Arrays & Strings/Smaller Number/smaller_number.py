#How many Numbers are the smaller number than the Current Number

#Nested loops

def smaller_than_current(nums):
    result = []

    for i in range(len(nums)):
        count = 0

        for j in range(len(nums)):
            if nums[i] > nums[j]:
                count += 1

        result.append(count)

    return result

nums = [9,7,5,3,1]

print(smaller_than_current(nums))