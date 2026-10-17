#for loop

s = "I will become an AI Engingeer"

reverse = ""

w = s.split()

for i in range(len(w)-1,-1,-1):
    reverse += w[i] + " "
print(reverse)
