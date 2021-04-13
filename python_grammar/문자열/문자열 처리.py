#문자열 연결
hello = '안녕' * 5
print(hello)


#문자열과 숫자 연결위해 str()이용
eng = 80
result = '영어 점수' + str(eng)+'점'
print(result)


# %연산자를 이용한 문자열 포맷팅
name = '오이'
print('나는 %s입니다.'%name)


#정수형 숫자 0으로 채우기
year = 2021
month = 3
day = 19
print('%d-%02d-%02d'%(year, month, day))
#02d는 정수형 숫자 두자리, 남는 부분은 0으로 채운다는 뜻


#str.format()문자열 포맷팅
name = '오이'
age = 27
height = 169
print('이름: {0}, 나이: {1}, 키: {2}'.format(name, age, height))