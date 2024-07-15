n=int(input())
grp=0
for _ in range(n):
    word=input()
    for j in range(len(word)):
        if j !=len(word) -1:
            if word[j]==word[j+1]:
                continue
            elif word[j] in word[j+1:]:
                break
        else:
            grp+=1
print(grp)
