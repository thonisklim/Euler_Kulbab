n = 2_000_000
c = 2
# найти сумму всех простых чисел до 2_000_000
# здесь решение перебором делителей от 2 до половины х


def isprime(x):
    for i in range(2, (x//2)+1):
        if x % i == 0:
            return False
    return True


for k in range(3, n, 2):
    if isprime(k):
        c += k
        print(k, c)

print(f"Answer: {c}")
