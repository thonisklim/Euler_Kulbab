c = 1
n = 20

for k in range(1, n + 1):
    a, b, i = k, c, 2
    while i <= a != 1 and i < k // 2 + 1:
        if a % i == b % i == 0:
            a //= i
            b //= i
        else:
            i += 1
        print('-', k, a, i)
    c *= a
    print(k, c)

print(f"Answer: {c}")
#for 30 = 2329089562800