

def creatematrix():
    ar = []
    print("columns = ")
    c = input()
    c = int(c)
    print("rows = ")
    r = input()
    r = int(r)
    for i in range(c):
        tempar = []
        k = 0
        for j in range(r):
            print(f"a{i}{j} = ")
            s = input()
            try:
                tempar.append(int(s))
                k += 1
            except ValueError:
                for t in s.split():
                    try:
                        tempar.append(int(t))
                        k += 1
                    except ValueError:
                        pass
            if k >= r:
                break
        ar.append(tempar)
    return ar


a = creatematrix()
print(a)