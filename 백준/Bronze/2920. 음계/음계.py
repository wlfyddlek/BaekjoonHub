melody=list(map(int,input().split()))

asc_melody=melody[:]
des_melody=melody[:]
asc_melody.sort()
des_melody.sort(reverse=True)

if melody==asc_melody:
    print("ascending")

elif melody==des_melody:
    print("descending") 

else:
    print("mixed")