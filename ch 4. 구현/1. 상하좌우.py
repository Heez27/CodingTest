# Q1. 상하좌우
# 여행가 A가 L, R, U, D 중 하나의 문자가 반복적으로 적혀있는 계획서를 보고 이동한다.
# nxn 크기의 정사각형 공간을 벗어나는 움직임은 무시한다.
# (L: 왼쪽으로 한 칸 이동, R: 오른쪽으로 한 칸 이동, U: 위로 한 칸 이동, D: 아래으로 한 칸 이동)

# A1) 내 코드
n = int(input('공간의 크기: '))
plan = list(input('여행 계획: ').split())
loc = [1,1] # 여행자의 현재 위치
for i in plan:
    if i == 'L' and loc[1]>1:
        loc[1] -= 1
    elif i == 'R' and loc[1]<n:
        loc[1] += 1
    elif i == 'U' and loc[0]>1:
        loc[0] -= 1
    elif i == 'D' and loc[0]<5:
        loc[0] += 1

print('여행자의 현재 위치는 [{},{}]'.format(loc[0],loc[1]))


# # A2) 교재 코드 변형
#
# n = int(input('공간의 크기: '))
# plans = list(input('여행 계획: ').split())
# loc = [1,1] # 여행자의 현재 위치
#
# move_types = ['L', 'R', 'U', 'D']
# dx = [0, 0, -1, 1]
# dy = [-1, 1, 0, 0]
#
# temp_x = 1
# temp_y = 1
# for plan in plans:
#     for i in range(len(move_types)):
#         # 임시로 이동해본 좌표
#         if plan == move_types[i]:
#             temp_x = loc[0] + dx[i]
#             temp_y = loc[1] + dy[i]
#
#     if temp_x<1 or temp_y<1 or temp_x>n or temp_y>n:
#         continue
#     else:
#         loc[0], loc[1] = temp_x, temp_y
#
#
# print('여행자의 현재 위치는 [{},{}]'.format(loc[0],loc[1]))