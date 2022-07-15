num1 = 600851475143
num2 = num1
#found prime
k = 2
t = 1

def isprime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True

while k <= num2:
    if num2 % k == 0:
        if isprime(k):
            t = k
        num2 //= k
        if num2 <= num1 // 2 + 1:
            if isprime(num2):
                t = num2
                break
    else:
        k += 1
    print(k, num2, t)

print(f"Answer: {t}")