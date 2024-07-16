a=[]
a=[list(map(int,input().split()))for _ in range(10)]
x,y= 1,1
while True:
    if(a[x][y]==0):
        a[x][y]=9
    elif(a[x][y]==2):
        a[x][y]=9
        break
    if(a[x+1][y]==1 and a[x][y+1]==1):
        break
    if(a[x][y+1]!=1):
        y=y+1
    elif(a[x+1][y]!=1):
        x=x+1
for i in range(10):
    for j in range(10):
        print(a[i][j],end=' ')
    print()