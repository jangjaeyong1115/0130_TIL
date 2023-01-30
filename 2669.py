matrix = [[0] * 100 for _ in range(101)]

cnt = 0

for i in range(4):
    x1,x2,y1,y2 = map(int,input().split())

    for t in range(x1,y1):
        for y in range(x2,y2):
            if matrix[t][y] == 0:
                matrix[t][y] += 1
                cnt += 1

    print(cnt)    