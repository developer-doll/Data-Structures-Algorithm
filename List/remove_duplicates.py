n = [6,4,5,3,7,7,6,3,1,0,5,8]
result = []

for num in n:
    if num not in result:
        result.append(num)

print(result)