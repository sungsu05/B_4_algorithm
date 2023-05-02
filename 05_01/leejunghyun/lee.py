
#옷가게 할인 받기

def solution(price):
    if price >= 500000:
        return(price*0.8) # 0.2를 하면 얼마나 할인을 하는지 나온다.   
    elif price >= 300000:
        return(price*0.9)# 10% 할인 0.1
    elif price >= 100000:
        return(price*0.95)# 5% 할인 0.5
    else:
        return(price)


solution(580000)    