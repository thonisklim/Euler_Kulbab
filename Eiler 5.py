c = 1
n = 30


def isprime(x):
    for p in range(2, (x//2)+1):
        if x % p == 0:
            return False
        print('-')
    return True


for k in range(1, n + 1):
    if not isprime(k):
        a, b, i = k, c, 2
        while i <= a != 1 and i < k // 2 + 1:
            if a % i == b % i == 0:
                a //= i
                b //= i
                if isprime(a):
                    i = a
            elif a % i == 0 and isprime(a):
                break
            else:
                i += 1
            print('-', k, a, i)
        c *= a
    else:
        c *= k
    print(k, c)

print(f"Answer: {c}")
