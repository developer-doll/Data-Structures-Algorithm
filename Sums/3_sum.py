def three_sums(nums,target):
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                if nums[i] + nums[j] + nums[k] == target:
                    return [i,j,k]
    
    return []

nums = [2,3,6,8,9,1]
target = 17

print(three_sums(nums,target))
