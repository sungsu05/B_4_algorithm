# https://www.acmicpc.net/problem/25304
""" 
영수증
시간 제한	메모리 제한	제출	정답	맞힌 사람	정답 비율
1 초	1024 MB	66461	37535	33839	57.534%
문제
준원이는 저번 주에 살면서 처음으로 코스트코를 가 봤다. 정말 멋졌다. 그런데, 몇 개 담지도 않았는데 수상하게 높은 금액이 나오는 것이다! 준원이는 영수증을 보면서 정확하게 계산된 것이 맞는지 확인해보려 한다.

영수증에 적힌,

구매한 각 물건의 가격과 개수
구매한 물건들의 총 금액
을 보고, 구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하는지 검사해보자.

입력
첫째 줄에는 영수증에 적힌 총 금액 
$X$가 주어진다.

둘째 줄에는 영수증에 적힌 구매한 물건의 종류의 수 
$N$이 주어진다.

이후 
$N$개의 줄에는 각 물건의 가격 
$a$와 개수 
$b$가 공백을 사이에 두고 주어진다.

출력
구매한 물건의 가격과 개수로 계산한 총 금액이 영수증에 적힌 총 금액과 일치하면 Yes를 출력한다. 일치하지 않는다면 No를 출력한다.

제한
 
$1 ≤ X ≤ 1\,000\,000\,000$ 
 
$1 ≤ N ≤ 100$ 
 
$1 ≤ a ≤ 1\,000\,000$ 
 
$1 ≤ b ≤ 10$ 
---
예제 입력 1 (영수증 형태)
260000
4
20000 5 
30000 2
10000 6
5000 8

예제 출력 1 
Yes
영수증에 적힌 구매할 물건들의 목록으로 계산한 총 금액은 20000 × 5 + 30000 × 2 + 10000 × 6 + 5000 × 8 = 260000원이다. 이는 영수증에 적힌 총 금액인 260000원과 일치한다. 
---
예제 입력 2 (영수증 형태)
250000
4
20000 5
30000 2
10000 6
5000 8

예제 출력 2 
No
"""
# 영수증의 맨위에 input()함수를 사용하여 값을 입력했을 때 *총 금액*과 *구매한 상품의 개수*를 읽어들이게 한다
total_amount = int(input())  # 총 금액
n = int(input())  # 구매한 상품의 개수

# 그런 다음 각 품목의 가격과 수량에서 총 금액을 계산하기 위해
# 변수의 초기값을 0으로 선언
calculated_total_amount = 0

# 구매한 각 상품을 영수증 입력 예시처럼 배열하기 위해
for i in range(n):
    price, quantity = map(int, input().split(" "))
    # split() : 입력되는 상품 가격과 수량을 공백으로 구분하고 문자열 목록으로 분할하기 위해 split()
    # map() : 상품의 가격과 수량이 담긴 문자열 리스트에서 / map()은 변환된 정수를 생성하는int()함수를 계산하는 반복기인 셈
    # int() : 리스트의 각 문자열을 정수형으로 형변환
    # 배열을 unpacking하여 반복되는 첫번째 정수를 price 변수에 할당, 두번째 정수를 quantity 변수에 할당
    # 즉 map(int, input().split()) : 공백으로 구분된 한 줄의 입력에서 두 개의 정수를 읽는 데 사용
    calculated_total_amount += price * quantity  # 가격과 현재 품목의 수량을 곱하여 계산된 총 금액에 추가

# 계산된 총 금액과 영수증에 입력된 총 금액을 비교
if calculated_total_amount == total_amount:
    print("Yes")  # "Yes"
else:
    print("No")  # "No"





# total_amount = 260000
# n = 4
# items = [(20000, 5), (30000, 2), (10000, 6), (5000, 8)]

# calculated_total_amount = 0
# for price, quantity in items:
#     calculated_total_amount += total_amount * quantity

# if calculated_total_amount == total_amount:
#     print("Yes")
# else:
#     print("No")
# 파이썬 터미널에서 실행하지 못해 따로 작성한 식입니다.
