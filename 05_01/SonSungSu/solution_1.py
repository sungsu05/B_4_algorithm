# 문제 : 피자 나눠 먹기(2)
# https://school.programmers.co.kr/learn/courses/30/lessons/120815?language=python3
##
def solution(n):
    for i in range(1,101):
        if i*6 % n == 0:
            return i
print(solution(6))
print(solution(10))
print(solution(4))


