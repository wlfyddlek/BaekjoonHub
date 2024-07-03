import sys
input=sys.stdin.readline
n=int(input())
for _ in range(n):
    a,b=map(str,input().split())
    sort_a=sorted(list(a))
    sort_b=sorted(list(b))

    if sort_a==sort_b:
        print(f"{a} & {b} are anagrams.")
    else:
        print(f'{a} & {b} are NOT anagrams.')