a, b = input().split()

a = list(map(int,a))
b = list(map(int,b))
print(sum(a) * sum(b))

# 1. 두 수를 입력받아 list형태로 A,B를 정의한다. ex) A=['1','2','3'], B=['4','5']

#2. A와 B, 리스트의 문자열을 int형태로 변환해준다. ex) A=[1,2,3], B=[4,5]

# 3. A의 sum과 B의 sum을 곱하여 출력한다.