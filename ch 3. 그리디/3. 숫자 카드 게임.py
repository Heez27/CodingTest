# Q3) N x M 형태로 카드들이 놓여있다고 가정할 때, 각 행의 가장 작은 값들 중 가장 큰 값의 카드를 찾아야함
# 입력조건: 행의 갯수 n과 열의 갯수 m을 공백을 기준으로 각각 자연수로 입력값을 받는다.
# 출력조건: 각 행의 가장 작은 값의 카드들 중 가장 큰 값을 출력해야함

# A1) min(list이름), max(list이름) 이용: list가 2가지(행을 담을 list, 각 행의 최솟값들을 담을 list)
n, m = map(int, input('N x M 행렬의 N값과 M값을 입력하시오: ').split())
row = [] # 각 행의 최솟값을 담을 리스트

for i in range(n):
    data = map(int, input('%d행을 입력하시오: '%(i+1)).split()) # 각 행의 m개의 데이터 입력
    row.append(min(data)) # 현재 행의 가장 작은 수 찾기

print('각 행의 가장 작은 값들 중 가장 큰 값의 카드는 %d이다. '%(max(row)))


# # A2) min(list이름), max(n1, n2)로 n1과 n2중 최댓값찾기: list가 1가지 + 최종값을 result로 두기
# n, m = map(int, input('N x M 행렬의 N값과 M값을 입력하시오: ').split())
# result = 0 # 최종값
# for i in range(n):
#     data = map(int, input('%d행을 입력하시오: '%(i+1)).split()) # 각 행의 m개의 데이터 입력
#     result = max(result, min(data)) # result와 data 중 최댓값 넣기
#
# print('각 행의 가장 작은 값들 중 가장 큰 값의 카드는 %d이다. '%(result))