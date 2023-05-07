# https://www.acmicpc.net/problem/20499
# 문제 : 다리우스님 한타 안 함?

# x = list(map(int,input().split('/')))
# print("hasu"if x[1]==0 or x[0]+x[2] < x[1] else "gosu")

print("hasu" if (lambda k,d,a: True if d == 0 or k+a < d else False)(*list(map(int,input().split('/')))) else "gosu")
