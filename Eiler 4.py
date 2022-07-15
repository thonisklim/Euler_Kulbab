import itertools

a = 1
b = 1
c = 0


def isPalindrom(x):
    i = 0
    n = x
    while n != 0:
        n //= 10
        i += 1
    while i > 1:
        if x // 10 ** (i - 1) == x % 10:
            x %= 10 ** (i - 1)
            x //= 10
            i -= 2
        else:
            return False
    return True

#zip afer 'in' will go 100 100, 101 101, 102 102
#itertools.product after 'in' will go 100 100, 100 101, 100 102


for a, b in itertools.product(range(100, 1000), range(100, 1000)):
    if isPalindrom(a * b) and a * b > c:
        c = a * b
print(f"Answer: {c}")