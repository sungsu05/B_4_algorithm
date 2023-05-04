def solution(n):
    answer = [] # 빈리스트를 사용
    
    for i in range(n+1): # 1부터 시작 , n까지 1증가 하기위해 사용
        if i % 2 == 1: # 홀수 값의 나머지가 1이 나오도록 함.
            print(i)
            answer.append(i)
    
    return answer
solution(10)