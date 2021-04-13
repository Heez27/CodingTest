#문자열 출력
name = 'Heez'
age = 27
height = 169

#1. 콤마(,)를 이용한 출력
print(name, age, height)


#기호 +를 이용한 출력
print('name= '+name+', height= '+str(height))


#문자열 포맷팅 %를 이용한 출력
print('이름, 나이, 키: %s, %d, %d'%(name, age, height))

#format()을 이용한 출력
print('이름: {}'.format(name))


#키워드 sep을 이용한 출력
print(name, age, height, sep='/')


#키워드 end를 이용한 출력
print(name, end='')