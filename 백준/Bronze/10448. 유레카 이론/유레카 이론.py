tri = [n * (n + 1) // 2 for n in range(45)]

b = int(input())

for _ in range(b):
    a = int(input())
    find = False 

    if a <= 1000:
        for i in range(1, 45):
            for j in range(i, 45):
                for k in range(j, 45):
                    total = tri[i] + tri[j] + tri[k]
                    if a == total:
                        find = True
                        break
                if find:
                    break
            if find:
                break
    
    
    if find:
        print(1)
    else:
        print(0)
