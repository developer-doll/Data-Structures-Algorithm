s1 = "earth"
s2 = "heart"

count1 = {}
count2 = {}

for ch in s1:
    if ch in count1:
        ch += 1
    else:
        ch = 1

for ch in s2:
    if ch in count2:
        ch += 1
    else:
        ch = 1

if count1 == count2:
    print("Anagram")
else:
    print("Not an Anagram")
         