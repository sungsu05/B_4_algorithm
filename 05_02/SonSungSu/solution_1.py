# https://school.programmers.co.kr/learn/courses/30/lessons/120818
# 옷가게 할인 받기

# 필요 개념
# 자리수 마다 ,(콤마) 넣는 방법
# num = 15000000
# print(format(num,','))
# 15,000,000

# 문자열 입력값의 ,(콤마) 를 제거하는 방법 + 형변환
# test = '150,000'
# test = int(test.replace(',',''))
# print(test,type(test))

# 단 이문제의경우 입력 예시는 문자열이지만, int형 자료형이 입력되고 있다.

def solution(price):
    if price >= 500000:
        result = format(int(price*0.8),',')
    else :
        result = format(int(price*0.9 if price>=300000 else price * 0.95),',')
    return result

# 입력값이 문자열일 경우

def solution_2(price):
    price = int(price.replace(',',''))
    result = ''
    if price >= 500000:
        result = format(int(price*0.8),',')
    else :
        result = format(int(price*0.9 if price>=300000 else price * 0.95),',')
    return result

# ... result 는 str인데 결과값은 int형으로 달라고 한다..
# 반례 1. 할인적용 삼품이 아닐경우를 고려
# 반례 2. 제한사항 1. 1의자리를 0으로 치환

def solution_3(price):
    if price < 100000:
        result = price
    elif price >= 500000:
        result = int(price*0.8)
    else :
        result = int(price*0.9 if price >= 300000 else price * 0.95)

    if result % 10 != 0:
        result = result - result % 10
    return result

# 반례 2 인경우, 바꾸라는말이아닌 입력값이 1의자리가 0으로 주어진다는 소리인듯

def solution_4(price):
    result = price
    if price >= 500000:
        result = price*0.8
    elif price >= 100000:
        result = price*0.9 if price >= 300000 else price * 0.95
    return int(result)


## 코드 축약

def solution_5(price):
    if price >= 500000:
        price = price*0.8
    elif price >= 100000:
        price = price*0.9 if price >= 300000 else price * 0.95
    return int(price)

a = 150000
b = 580000
# print(solution(a))
# print(solution(b))
print(solution_4(a))
print(solution_4(b))

a = '150,000'
b = '580,000'
# print(solution_2(a))
# print(solution_2(b))
