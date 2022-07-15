import itertools

a = 0
b = 0
c = 0
#c **= 1/2

for a, b in itertools.product(range(1, 1000), range(1, 1000)):
    c = a**2 + b**2
    c **= 1/2
    if a + b + c == 1000:
        print(a, b, c)
        break
print(a*b*c)
