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

# 시간 초과
def solution(ingredient):
    ingredient = "".join(map(str,ingredient))
    result = 0
    while '1231' in ingredient:
        result += 1
        ingredient = ingredient.replace('1231','',1)
    return result

def solution_2(ingredient):
    buger = '1231'
    s = ''.join(list(map(str, ingredient)))
    result = 0
    while buger in s:
        if s.find(buger) >= 4:
            # print(s,s.find('1231'))
            s = s[s.find(buger)-4:]
            # print(s,s.find('1231'))
        s = s.replace(buger,'',1)
        result += 1
    return result
# 132121312222222222122221231231 , 22 -4
# 22221231 , 4

# -4를 하는 이유
# 1, 3, 2, 1, 2, 1, 3, 1, 2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,1,1,2,3,1,2,3,1
# 1, 3, 2, 1, 2, 1, 3, 1, 2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,1,1,2,3,1,2,3,1
# 22211231231
# '1231'을 잘라내고, 잘라낸 이전 값에서 새로운'1231'의 값이 생길 수 있다.


# x = [2, 1, 1, 2, 3, 1, 2, 3, 1]
# print(solution(x))
# print(solution_2(x))

x = [1, 3, 2, 1, 2, 1, 3, 1, 2,2,2,2,2,2,2,2,2,2,2,1,2,2,2,1,1,2,3,1,2,3,1]
# print(solution(x))
print(solution_2(x))

x =[1,1,2,3,1,2,3,1,2,3,1,2,3,1]
# print(solution_2(x))
# print(solution(x))



# x = "012345123"
# print(x.find('1'))
# print(x.index('1'))
# x = x.replace('123','',1)
# print(x)

# string = '712317771231888'
# result = string.find('1231')
# print(result)
# s = string[string.find('1231')-4:] # 3-4 = -1
#
# print(s)