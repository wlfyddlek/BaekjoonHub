n=int(input())


f=[0]*117
f[1]=f[2]=f[3]=1
for i in range(4,n+1):
    f[i]=f[i-3]+f[i-1]
print(f[n])
