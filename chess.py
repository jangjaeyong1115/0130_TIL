import pprint
matrix = []

for _ in range(8):
    matrix.append(list(input()))

pprint.pprint(matrix)

# list comprehension
matrix = [list(input()) for _ in range(8)]

# 2. 3x3
matrix = [list(map(int,input().split())) for _ in range(3)]
