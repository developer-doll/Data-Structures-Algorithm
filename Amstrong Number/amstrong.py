n = 153

temp = n

digits = len(str(n))

total = 0

while temp > 0:
    digit = temp % 10
    total += digit ** digits
    temp //= 10

if total == n:
    print(f"{n} is Amstrong")
else:
    print(f"{n} is not an Amstrong")