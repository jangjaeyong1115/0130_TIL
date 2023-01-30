list = []

for i in range(5):
    list.append(sum(map(int,input().split())))

print(list.index(max(list))+1,max(list))