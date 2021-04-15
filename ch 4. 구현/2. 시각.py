# Q2) 시각
# 정수 N이 입력되면 00시 00분 00초부터 N시 59분 59초까지의 모든 시각 중에서 3이 하나라도 포함되는
# 모든 경우이 수를 구하는 프로그램을 작성하시오. (단, 0<=N<=23)
# ex) 00시 00분 03초, 00시 13분 30초는 3이 포함되어있음
# ex2) 00시 02분 55초, 01시 27분 45초는 3이 포함되어 있지 않음
# 실행결과: N = 5일때, 11475

# A1) 내 코드
# n = input('N시를 입력하시오: ')
# count = 0
#
# for i in range(int(n)+1):
#     for j in range(60):
#         for k in range(60):
#             time = str(i)+str(j)+str(k)
#             if time.find('3') != -1:
#                 count += 1
#
# print(count)



# A2) 교재 코드 변형

n = input('N시를 입력하시오: ')
count = 0

for i in range(int(n)+1):
    for j in range(60):
        for k in range(60):
            time = str(i)+str(j)+str(k)
            if '3' in str(i)+str(j)+str(k): #여기만 다름
                count += 1

print(count)