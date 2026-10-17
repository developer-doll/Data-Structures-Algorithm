#For loop
p = "MADAM"

reverse = ""

for ch in p:
    reverse += ch 

# print(reverse)

if p == reverse:
    print("true")
else:
    print("false")


#Two Pointers
p1 = list("MALAYALA")

left = 0
right = len(p1) -1 

while left < right:
    if p1[left] != p1[right]:

        left += 1
        right -= 1

        print("Not a Palindrome")
        break

    else:
        print("Palindrome")
        break


