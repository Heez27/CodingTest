# # 다시 풀어야함!!
#
# n, m = map(int, input('nxm행렬의 n과 m: ').split()) # nxm 맵 생성
# x, y, direction = map(int, input('위치와 방향(0: 북쪽, 1: 동쪽, 2: 남쪽, 3: 서쪽): ').split())
#
# matrix = [] # nxm 행렬
# for i in range(n): # 0: 육지, 1: 바다
#     row = list(input('row %d: '%(i)).split())
#     matrix.append(row)
#
# count = 0 # 이동 횟수
# route = [] # 가본 칸들
#
# steps = [(-1,0), (0,1), (1,0), (0,-1)] # 순서대로 북, 동, 남, 서 (시계)방향
#
# # 1. 현재 위치에서 현재 방향을 기준으로 왼쪽 방향(반시계 방향으로 90도 회전한 방향)부터 차례대로 갈 곳을 정한다.
# # 2. 캐릭터의 바로 왼쪽 방향에 아직 가보지 않은 칸이 존재한다면, 왼쪽 방향으로 회전한 다음 왼쪽으로 한 칸을 전진한다.
# #    왼쪽 방향에 가보지 않은 칸이 없다면, 왼쪽으로 회전만 수행하고 1단계로 돌아간다.
# # 3. 만약 네 방향 모두 이미 가본 칸이거나 바다로 되어 있는 칸인 경우에는, 바라보는 방향을 유지한 채로 한 칸 뒤로 가고
# #    1단계로 돌아간다. 단, 이때 뒤쪽 방향이 바다인 칸이라 뒤로 갈 수 없는 경우에는 움직임을 멈춘다.
#
# while True:
#     for i in range(4): # 임시로 왼쪽 방향으로 움직여봄
#         step = steps[direction-i-1]
#         temp_x = x + step[0]
#         temp_y = y + step[1]
#
#         if (temp_x, temp_y) not in route and matrix[temp_x][temp_y] != 1: # 가보지 않았고, 바다가 아닌 경우
#             # 왼쪽으로 한칸 전진
#             x = temp_x
#             y = temp_y
#             route.append((x,y))
#             count += 1
#         else:
#             direction -= 1 # 왼쪽으로 돌기(반시계 방향으로)
#             continue # 아무것도 안함
#
#     if i == 3 and
#
#
#
# # while True:
# #     for i in range(4): # 임시로 왼쪽 방향으로 움직여봄
# #         step = steps[direction-i+1]
# #         temp_x = x + step[0]
# #         temp_y = y + step[1]
# #
# #         if matrix[temp_x][temp_y] == 1 and (temp_x, temp_y) in route: # 임시로 움직여 본게, 바다인 경우나 가본 곳일 경우
# #             step = steps[direction-2] # 임시로 바라보는 방향을 유지한 채로 한 칸 뒤로 가본다.
# #             temp_x = x + step[0]
# #             temp_y = x + step[1]
# #             if matrix[temp_x][temp_y]==1: #임시로 바라보는 방향을 유지한 채로 한 칸 뒤로 가본게 바다일 경우 움직임을 멈춘다.
# #                 break
# #             else:
# #                 x = temp_x
# #                 y = temp_y
# #                 route.append((temp_x, temp_y))  # 가본 곳에 추가
# #                 count += 1
# #         elif matrix[temp_x][temp_y] == 1: # 그냥 바다인 경우, 아무것도 안함
# #             continue
# #         elif (temp_x, temp_y) in route: # 가본 곳일 경우, 아무것도 안함
# #             continue
# #         else:   # 육지인 경우 이동
# #             x = temp_x
# #             y = temp_y
# #             route.append((temp_x,temp_y)) # 가본 곳에 추가
# #             count += 1
# #             break # for문 탈출
