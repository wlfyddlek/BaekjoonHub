a=[int(input()) for _ in range(9)]

sum=sum(a)
for i in range(9):
    for j in range(i+1,9):
        if sum-a[i]-a[j]==100:
            for k in range(9):
                if k not in [i,j]:
                    print(a[k])
