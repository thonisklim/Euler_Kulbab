# алгоритм факторизации числа "Перебор делителей (пробное деление)"
def natdiv(k):
    nd = 2
    for i in range(2, int(k ** .5 // 1) + 1):
        if k % i == 0:
            nd += 2
    return nd


print(natdiv(76576500))
