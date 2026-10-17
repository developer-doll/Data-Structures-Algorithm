#Prime

# n = int(input("Check Prime : "))
n = 7

if n < 2:
    print("Not a Prime")
else:
    prime = True

    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            prime = False
            break
    print("Prime" if prime else "Not a Prime Number")
    