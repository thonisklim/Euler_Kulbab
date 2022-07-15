n = 2_000_000
c = 2
a = []
# найти сумму всех простых чисел до 2_000_000
# в а хранятся простые числа


def isprime(x):
    if x < 200:
        for i in range(2, (x//2)+1):
            if x % i == 0:
                return False
    else:
        for i in range(2, 100):
            if x % i == 0:
                return False
        for j in range(len(a)):
            if x % a[j] == 0:
                return False
    return True


for k in range(3, n, 2):
    if isprime(k):
        c += k
        a.append(k)
        print(k, c)

print(f"Answer: {c}")
