a = 0
b = 1
s = 0
const = 4*10**6
while b < const:
    if b % 2 == 0:
        s += b
    a, b = b, a + b
print(s)
