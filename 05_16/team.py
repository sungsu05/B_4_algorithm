# 팀 재편성
# 시스템 1 : 팀은 1~20 팀 까지 있음
# 시스템 2 : 각 팀당 팀원 5명이 있음
# 시스템 3 : 팀원 전원이 팀 해체를 원하지 않을시, 팀 유지가 됨
# 시스템 4 : 팀원 중 단 한 명이라도 팀 유지를 원하지 않을시 팀은 해체됨
# 시스템 5 : 재편성이 필요한 학생은, 원하는 짝꿍을 한 명 선택 할 수 있다.


# 문제 1. 유지된 팀이 만약 13번 팀이라면, 다음 팀도 13번 팀으로 할 것인가?
# list에 기억하는 방식으로 하면 구현이 가능할 것 같으나, 재 편성 하도록 해보자.

# 문제 2. 테스트 케이스 데이터를 어떻게 구현할 것인가?
# faker 를 이용한 테스트 케이스 데이터 생성
# 얼마나 생성할 것인가? > 우선은 10개 팀만 생성하도록 하자.
# 리스트의 형식 > 1차원 배열  = 팀 번호 , 2 차원 배열 = 학생들

# 문제 3. A 라는 학생과 팀이 되길 원하는 학생이 5명 이상이라면?
# random.choice 를 통해 선별한다.

# 문제 4. A라는 학생과 팀이 되길 원하지만, A는 이미 팀이 짜여져 있다면?
# A 학생과 팀이 될 수 없다.

# 문제 5. 얼마나 공정한가 ?
# 데이터를 순서대로 프로그램을 돌리다 보면, 공정하지 못하게 될 경우가 생길 것 같다.
# random 함수를 적절히 사용해서 순서를 정해보자.

# 알고리즘의 구현 순서

# 1. faker를 이용한 2차원 배열 만들기
# 2. class를 활용해 name,target_name,reshuffle 변수 만들기
        # name = self의 이름
        # target_name = self가 같은 팀이 되고 싶어하는 학생의 리스트 index 번호
        # reshuffle = 재편성 희망 True and False로 설정
#    target_name에 데이터를 입력해야하니, for문을 한 번더 도는것보다
#    빈 리스트를 미리 생성하고, target_name에는 해당하는 index값을 저장하자.
        # 따라서 target_name의 변수 이름을 target_list_index 로 변수 이름 변경

from faker import Faker
import random

# 상수 전역 변수
FAKE = Faker("ko_KR")
MAX_TEAM = 10
# 최대 팀 개수
MAX_MEMBERS = 5
# 팀당 최대 몇명이 포함될것인지?

class Student():
    def __init__(self,name,my_code,target_code,reshuffle):
        self.name = name
        self.reshuffle = reshuffle

def check_team_reshuffle(arr):
    for i in range(len(arr)):
        if not arr[i].reshuffle:
            return False
    return True



team_sparta =list([None]*MAX_MEMBERS for _ in range(MAX_TEAM))
result = []
# 스파르타 팀 초기값, 빈 리스트 생성 type은 문자열
# fix > 이렇게 하지 말고, target_list_index는 random 메서드 사용

# 테스트 케이스 만들기
# result = text_01.zfill(2)+text_02.zfill(2)
for i in range(MAX_TEAM):
    for j in range(MAX_MEMBERS):
        team_sparta[i][j] = Student(
            name= FAKE.name(),
            my_code = str(i).zfill(2) + str(j).zfill(2),
            target_code = str(random.randint(0,MAX_TEAM)).zfill(2) + str(random.randint(0,MAX_MEMBERS)).zfill(2),
            reshuffle= random.choice([True,False])
        )



students = []

# 팀원 모두가 팀을 이어가길 선택했는지 판단
# 모두가 이어가길 선택했으면 바로 결과값에 2차원 리스트 형태로 결과값을 넣는다
# 아니라면 1차원 배열 students에 삽입
for i in range(len(team_sparta)):
    if check_team_reshuffle(team_sparta[i]):
        result.append(team_sparta[i])
    else:
        students += team_sparta[i]

# 팀원이 정해지지 않은 사람들 순서 섞기
random.shuffle(students)

# 남은 데이터
# 남아있는 사람 들의 선호도를 고려한 짝꿍 정하기

# 현재 단계에서 구할 수 있는 것
# students // MAX_MEMBERS 의 값  = 앞으로 구해야할 팀 개수
team_sparta =list([None]*MAX_MEMBERS for _ in range(len(students)//MAX_MEMBERS))
# len(reuslt) : 정해진 팀 개수
# len(team_sparta) : 정해야 할 팀 개수


# 남은 팀원 정하기
#  A 그룹 : 내가 같은 팀이 되고 싶은 사람이, 아직 팀이 정해지지 않았을 경우 << 선호하는 사람과 팀이 되어야 한다.
#  B 그룹 : 내가 같은 팀이 되고 싶은 사람이, 이미 팀이 정해진 경우 << 아무대나 들어가도 상관 없다


# A 그룹 먼저 팀 선정


# GG.. 자러가자




# 남은 자리는 B 그룹의 인원들이 입장

# 팀 편성 완료




