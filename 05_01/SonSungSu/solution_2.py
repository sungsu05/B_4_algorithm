# https://school.programmers.co.kr/learn/courses/30/lessons/120816
# 피자 나눠 먹기 3
def solution(x,y):
    result = int(y/x)
    return result if y % x == 0 else result + 1


a = 7
b = 10
print(solution(a,b))
a = 4
b = 12
print(solution(a,b))