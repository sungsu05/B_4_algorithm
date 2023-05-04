# https://school.programmers.co.kr/learn/courses/30/lessons/120819
# 문제 : 아이스 아메리카노
# 입력 예시는 쉼표가 있지만, 실제 입력은 int형으로 쉼표 없이 입력되고 있다.

def solution(money):
    return [money // 5500, money % 5500]

x = 5500
print(solution(x))
x = 15000
print(solution(x))
x = 3000
print(solution(x))