# 문제 n 값이 주어졌을때 n의 팩토리얼을 구하라!
# 반복문으로 구하기
n = 5
# 5 * 4 * 3 * 2 * 1
result = n
while True:
    n -= 1
    if n == 0:
        break
    result *= n

print(result)

#####################################################
# 재귀 함수로 구하기

def solution(n):
    if n == 1:
        return 1
    return n * solution(n -1)

# 5 * solution(n-1)
# 4 * solution(n-1)  : 3
# 3 * solution(n-1)  : 2
# 2 * solution(n-1)  : 1
# 1 일때는 1을 리턴!

print(solution(n))