# https://school.programmers.co.kr/learn/courses/30/lessons/120818?language=python3
"""
문제 설명
머쓱이네 옷가게는 10만 원 이상 사면 5%, 30만 원 이상 사면 10%, 50만 원 이상 사면 20%를 할인해줍니다.
구매한 옷의 가격 price가 주어질 때, 지불해야 할 금액을 return 하도록 solution 함수를 완성해보세요.
이 구현에서는 먼저 가격이 50만원 이상인지 확인합니다.
그렇다면 20% 할인을 적용하고 함수를 사용하여 결과를 정수로 반환합니다 int().
가격이 50만원 이하일 경우 30만원 이상인지 확인하여 10% 할인을 적용합니다.
마찬가지로 가격이 100,000원을 초과하면 5% 할인을 적용합니다.
마지막으로 가격이 10만원 이하일 경우 할인 없이 원가로 돌려드립니다.
"""


def solution(price):
    if price >= 500000:
        answer = int(price * 0.8)
    elif price > 300000:
        answer = int(price * 0.9)
    elif price > 100000:
        answer = int(price * 0.95)
    else:
        answer = price
    return answer


test_cases = 500000  # 400000

#     (580000, 464000)
#     (100000, 100000)
#     (300000, 270000)
#     (500000, 400000)
#     (90000, 90000)
#     (600000, 480000)

print(solution(test_cases))
