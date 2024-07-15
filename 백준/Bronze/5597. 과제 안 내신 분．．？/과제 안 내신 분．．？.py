std=[i for i in  range(1,31)]
for i in range(28):
    remove=int(input())
    std.remove(remove)
print(min(std))
print(max(std))
