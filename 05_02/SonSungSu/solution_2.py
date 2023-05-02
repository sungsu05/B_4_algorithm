# https://school.programmers.co.kr/learn/courses/30/lessons/120813
# 문제 짝수는 싫어요
def solution(n):
    return [i for i in range(n+1) if i%2 != 0]

def solution_2(n):
    return [i for i in range(1,n+1,2)]

x = 10
print(solution(x))
print(solution_2(x))
x = 15
print(solution(x))
print(solution_2(x))