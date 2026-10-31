#Nested loops

def two_sums(nums,target):

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):

            if nums[i] + nums[j] == target:
                return [i,j]

    return []

nums = [2,4,5,6]
target = 7

print(two_sums(nums,target))