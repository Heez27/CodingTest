# Q2) 배열의 크기 N, 숫자가 더해지는 횟수 M, 그리고 연속으로 더할 수 있는 횟수 K가 주어질 때, 큰 수의 법칙에 따른 결과를 출력하시오.
#        입력조건: 1. 먼저, N, M, K을 받는다. 단, K<=M이다.
#                2. N개의 자연수의 입력을 받는다.
#        출력조건: 위의 큰 수의 법칙에 따라 더해진 답을 출력한다.

# 실행결과1: n, m, k = 5, 8, 3이고, 배열이 [2, 4, 5, 4, 6]일때, 결과는 46
# 실행결과2: n, m, k = 5, 7, 2이고, 배열이 [3, 4, 3, 4, 3]일때, 결과는 28

# A1) 내 코드

# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input('N, M, K를 공백으로 구분하여 입력받기: ').split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input('N개의 수를 공백으로 구분하여 입력받기: ').split())) # 위 방법에서, list()만 붙여주면 됨

data.sort() # 리스트 정렬하기

result = 0 # 결과값

for i in range(m):
    if (i+1)%(k+1)==0:
        result += data[-2] # 두 번째로 큰 수 더함
    else:
        result += data[-1] # 가장 큰 수 더함

print(result)


# #A2) 책 코드 변형
# n, m, k = map(int, input('N, M, K를 공백으로 구분하여 입력받기: ').split())
# data = list(map(int, input('N개의 수를 공백으로 구분하여 입력받기: ').split())) # 위 방법에서, list()만 붙여주면 됨
#
# data.sort() # 리스트 정렬하기
#
# first = data[n-1] # 가장 큰 수
# second = data[n-2] # 두 번째로 큰 수
#
# # 가장 큰 수 first가 더해지는 횟수 계산
# count = int(m/(k+1)) * k # (first* k번 + second)묶음 갯수에 k를 곱한 꼴. 한 묶음에 first를 k번 곱하므로
# count += m % (k+1) # 묶음을 제외한 나머지 부분
#
# result = 0 # 결과값
# result += first*count # 가장 큰 수  count번 더하기
# result += second*(m-count) # 두 번쨰로 큰 수 더하기
#
# print(result)