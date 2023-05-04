
#상수 재료 순서[야채,빵,빵,야채,고기,빵,야채,고기,빵]

#포장 [빵, 야채, 고기, 빵]
# 남은 재료  [야채, 빵, 야채, 고기, 빵]



# 보기 좋게 폭망..
# ingredient = [1, 2, 3, 1]
# def solution(ingredient):
#     answer=0
#     for i in ingredient:
#         if ingredient[i:i+4:1] == buger:
#             answer += 1
#             del ingredient[i:i+4:1]
#     return answer
# print(solution(ingredient))


# 빵 야채 고기 빵
# 야채 고기 빵
# 두 개 햄버거
# 아래서 부터 위로 쌓이게 된다.

ingredient = [2,1,1,2,3,1,2,3,1]
def solution(ingredient):
    a = 0

    stack = [] # 들어가는 재료를 넣기위해 

    for i in ingredient:
        if i == 1 and stack[-3:] == [1, 2, 3]: # 1 =1,2,3 을 먼저 보기 위해 사용했다. 
            del stack[-3:] #:-3뒤를 짜르기 위함
            a += 1
        else:
            stack.append(i)
    return a


solution(ingredient)



# stack = stack[:-3]
# del stack[-3:]


# a = [2,1,1,2,3,1,2,3,1]
# print(a[-3:])
# a = [2,1,1,2,3,1,2,3,1]
# print(a[:-3])

#  if i == 1 and stack[-3:] == [1,2,3]:
#     pass