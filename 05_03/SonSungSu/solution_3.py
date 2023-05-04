# https://school.programmers.co.kr/learn/courses/30/lessons/133502
# 햄버거 만들기

# 상수의 앞에 쌓이는 재료의 순서가 [ 야채, 빵, 빵, 야채, 고기, 빵, 야채, 고기, 빵]
# 여섯 번째 재료가 쌓였을 때, 세 번째 재료부터 여섯 번째 재료를 이용하여 햄버거를 포장하고
#  포장한거 [빵, 야채, 고기, 빵]
#  남은거   [야채, 빵, 야채, 고기, 빵]

# 야채 = 2
# 빵 = 1
# 고기 = 3

# x = [1,2,3]
# # x = [str(i) for i in x]
# # x = "".join(x)
# x = "".join([str(i) for i in x])
# print(x)

# 오답 : 반례 1,1,2,3,1,2,3,1,2,3,1,2,3,1
# def solution(ingredient):
#     buger = "1231"
#     ingredient = "".join(map(str,ingredient))
#     result = 0
#     while True:
#         if buger in ingredient:
#             print(ingredient)
#             result += ingredient.count('1231')
#             ingredient = ingredient.replace(buger,'')
#             print(ingredient)
#             continue
#         break
#     return result

def solution(ingredient):
    result = 0
    while True:
        for i in range(len(ingredient)):
            if ingredient[i:i+4] == [1,2,3,1]:
                del ingredient[i:i+4]
                result += 1
                continue
            break
    return 0

x = [2, 1, 1, 2, 3, 1, 2, 3, 1]
print(solution(x))
x = [1, 3, 2, 1, 2, 1, 3, 1, 2]
print(solution(x))
x =[1,1,2,3,1,2,3,1,2,3,1,2,3,1]
print(solution(x))

x = [2, 1, 1, 2, 3, 1, 2, 3, 1]
del x[0:0+4]
print(x)
