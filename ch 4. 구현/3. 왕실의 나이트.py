# Q3) 왕실의 나이트
# 8x8 좌표평면이 있고, 여행자는 말을 타고 있기 때문에 L자 형태로만 이동할 수 있다.
# 1. 수평으로 2칸 이동 뒤, 수직으로 한칸 이동 (총 4가지)
# 2. 수직으로 2칸 이동 뒤, 수평으로 한칸 이동 (총 4가지)
# [[a1,b1 ... , h1], [a2, b2, ..., h2], [a8, b8, ... ,h8]] 꼴의 행렬로 이루어져 있다.
# 현재 위치에서 여행자가 이동할 수 있는 경우의 수를 구하시오.

# 실행결과: a1을 넣으면 2
# 실행결과2: c2를 넣으면 6
# 실행결과3: h8을 넣으면 2


# # A1) 내 코드 : ord함수를 이용해, ascii코드를 숫자로 표현
#
# # 현재 위치 입력받기
# loc = input('현재 위치: ')
#
# # ord 함수로 현재 위치를 숫자로 바꾸기
# x = ord(loc[0])
# y = int(loc[1])
#
# count = 0 # 경로 수
#
# # 총 8가지의 경우가 있는데, 1번 경우로 4가지 경로, 2번 경우로 4가지 경로 만들어서 총 8가지 경로 가능
# # 1번 경우
# dx1 = [2, -2]
# dy1 = [1, -1]
#
# # 2번 경우
# dx2 = [1, -1]
# dy2 = [2, -2]
#
# # list index out of range 오류안뜨게 조심!! 이때, i와 j는 숫자가 아니야!!
# for i in dx1:
#     for j in dy1:
#         temp_x = x + i
#         temp_y = y + j
#         if temp_x< ord('a') or temp_x>ord('h') or temp_y<1 or temp_y>8: # 평면을 벗어난 경우
#             continue
#         count += 1 # 평면을 벗어나지 않은 경우
#
#
# for i in dx2:
#     for j in dy2:
#         temp_x = x + i
#         temp_y = y + j
#
#         if temp_x < ord('a') or temp_x > ord('h') or temp_y < 1 or temp_y > 8: # 평면을 벗어난 경우
#             continue
#         count += 1 # 평면을 벗어나지 않은 경우
#
#
# print(count)


# A2) 교재 코드 변형: 리스트에 튜플을 정의했을 때, for문 보기!!
loc = input('현재 위치: ')
x = ord(loc[0])-ord('a')+1
y = int(loc[1])

# 8가지 방향 정의
steps = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,2), (-1,-2), (1,2),(1,-2)]

count = 0 # 몇 가지 경로가 있는지

for step in steps:
    temp_x = x + step[0]
    temp_y = y + step[1]

    if temp_x<1 or temp_x>8 or temp_y<1 or temp_y>8:
        continue
    count += 1

print(count)