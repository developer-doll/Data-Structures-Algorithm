#For loop

s = "REDIS"

reverse = ""

for i in range(len(s)-1,-1,-1):
    reverse += s[i]

print(reverse)

#==============================================

#Two Pointers

s1 = list("DOCKER")

left = 0
right = len(s1) - 1

while left < right:
    s1[left],s1[right] = s1[right],s1[left]

    left += 1
    right -= 1

print("".join(s1))

#=================================================

#In-Built

s2 = "FASTAPI"
result = s2[::-1]
print(result)
