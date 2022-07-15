a = 1
i = 0
n = 10001


def isprime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True


while i < n:
    a += 1
    if isprime(a):
        i += 1
        #print(i, ':', a)

print(f"Answer: {a}")