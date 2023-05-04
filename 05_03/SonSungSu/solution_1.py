# https://school.programmers.co.kr/learn/courses/30/lessons/12945?language=python3
# 문제 : 피보나치의 수열

# 나의 학습 내용
# https://velog.io/@rumor/%ED%94%BC%EB%B3%B4%EB%82%98%EC%B9%98%EC%9D%98-%EC%88%98-Python

# 재귀 함수를 이용한 풀이
def solution(n):
    if n < 2:
        return n
    return solution(n-1) + solution(n-2)


def fibo(n,dp):
    if dp[n] == -1:
        dp[n] = fibo(n-1,dp) + fibo(n-2,dp)
    return dp[n]

def solution_2(n):
    dp = [-1] * 100001
    dp[0] = 0
    dp[1] = 1
    return fibo(n,dp)

def solution_3(n):
    dp = [0]*100001
    dp[1] = 1
    for i in range(2,n+1):
        dp[i] = dp[i-1] + dp[i-2]
        print(i, dp[i])
    return int(dp[n]%1234567)

# dp[0] , i = 0     ::   실행 없음 ,         dp[0] = 0
# dp[1] , i = 1     ::   실행 없음 ,         dp[1] = 1
# dp[2] , i = 2     ::   dp[2] = 1 + 0      dp[2] = 1
# dp[3] , i = 3     ::   dp[2] = 1 + 1      dp[2] = 2
# dp[4] , i = 4     ::   dp[2] = 2 + 1      dp[2] = 3
# dp[5] , i = 5     ::   dp[2] = 3 + 2      dp[2] = 5
# dp[6] , i = 6     ::   dp[2] = 5 + 3      dp[2] = 8
# dp[7] , i = 7     ::   dp[2] = 8 + 5      dp[2] = 13


print(solution(13))
print(solution_2(13))
print(solution_3(13))