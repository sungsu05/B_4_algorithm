# https://www.acmicpc.net/problem/25304
# 문제 : 영수증

# 새로 만든 코드
# 영수증에 적힌 금액
x = int(input())
print("Yes" if sum([(lambda a,b:a*b)(*list(map(int,input().split(' ')))) for i in range(int(input()))]) == x else "No")


# 기존 코드
# 영수증에 적힌 금액
x = int(input())
# 구매한 물건 종류의 수
n = int(input())

sum = 0
for i in range(n):
    a,b = map(int,input().split(' '))
    sum += a * b

print("Yes"if sum == x else "No")


""" 
입력 예시
250000
4
20000 5
30000 2
10000 6
5000 8
출력 : Yes

250000
4
20000 5
30000 2
10000 6
5000 8
출력 : No
"""