# https://school.programmers.co.kr/learn/courses/30/lessons/12945
# 참고 영상 https://www.youtube.com/watch?v=5C0IxOYVrhg
""" 
문제 설명

피보나치 수는 F(0) = 0, F(1) = 1일 때, 
1 이상의 n에 대하여 F(n) = F(n-1) + F(n-2) 가 적용되는 수 입니다.

예를들어

F(2) = F(0) + F(1) = 0 + 1 = 1
F(3) = F(1) + F(2) = 1 + 1 = 2
F(4) = F(2) + F(3) = 1 + 2 = 3
F(5) = F(3) + F(4) = 2 + 3 = 5
...
와 같이 이어집니다.

2 이상의 n이 입력되었을 때, n번째 피보나치 수를 
1234567으로 나눈 나머지를 리턴하는 함수, solution을 완성해 주세요.

제한 사항
n은 2 이상 100,000 이하인 자연수입니다.

입출력 예
n	return
3	2
5	5

입출력 예 설명
피보나치수는 0번째부터 0, 1, 1, 2, 3, 5, ... 와 같이 이어집니다.

+ 

0번째와 1번째 피보나치 수는 
입출력에 변화가 없는 0과 1이므로 
조건문을 사용해 0과 1은 수열계산에서 그대로 반환하도록 구현.

다음으로 입출력에 변화가 있는 피보나치 수열의 시작 지점을
0과 1을 갖는 리스트로 선언한다.
그 다음 루프를 사용하여 피보나치 수열의 증감식을 list.append로 구현.
1234567로 나눈 몫(n)을 구하기 위해 % 연산자 사용.
n 반환
"""
# version1


def fibonacci(n):
    if n < 2:
        return n

    fib_start = [0, 1]
    for i in range(2, n+1):
        # 입력된 수(n) 다음에 올 수(n-1)+(n-2)
        fib_start.append((fib_start[i-1] + fib_start[i-2]) % 1234567)

    return fib_start[n]


# for test
n = 5
result = fibonacci(n)
print(result)  # 5
