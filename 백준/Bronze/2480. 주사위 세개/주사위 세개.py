a,b,c= map(int,input().split())

if a==b==c:
    print(10000+a*1000)
elif a==b:
    print(1000+a*100)
elif b==c:
     print(1000+b*100)
elif a==c:
     print(1000+a*100)
else:
     if a>b:
          if a>c:
               print(a*100)
     if b>a:
          if b>c:
               print(b*100)
     if c>b:
          if c>a:
               print(c*100)
    