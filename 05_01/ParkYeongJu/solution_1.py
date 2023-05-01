# ㅡㅡㅡㅡㅡ 1. https://school.programmers.co.kr/learn/courses/30/lessons/120815 ㅡㅡㅡㅡㅡ
# 피자나눠먹기(2)
import math

def solution(n):
    # n과 6의 최소공배수
    lcm = abs(n * 6) // math.gcd(n, 6)
    return lcm//6 # lcm을 6으로 나눈다.