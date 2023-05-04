#https://www.youtube.com/watch?v=5C0IxOYVrhg


#피보나치
#fib(0) = 0
#fib(1) = 1     0과 1은 정의 해놓은 것 피보나치라는 사람이
#fib(n) = fib(n-1) + fib(n-2) 기본 정의

# 재귀함수의 기본동작 
# 재귀함수의 탈출조건 무한루프


def fib(num):

    # 기본동작
    return fib(num -1 ) + fib(num-2)
num = int(input())
print(fib(num))    