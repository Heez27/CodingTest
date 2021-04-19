# 코딩테스트

### ch1. 코딩테스트 개요


### ch2. 


### ch3. 그리디

##### 1) 그리디 Greedy 알고리즘(욕심쟁이 알고리즘): 현재 상황에서 지금 당장 좋은 것만 고르는 방법
   사전에 외우고 있지 않아도 풀 수 있을 가능성이 높은 문제 유형
   
```python
   # Q1) 그리디 알고리즘
   count_coin += N//coin # *조심하기* /는 결과가 실수, //는 결과가 정수
```
       
##### 2) 하지만, 가장 큰 화폐 단위가 나머지 화폐의 배수가 아니라면, 그리디 알고리즘으로 해결할 수 없다. 
 예를 들어, 화폐 단위가 500원, 400원, 100원 인 경우는, <br>
 그리디 방법: 800원 = 500원 + 100원 + 100원 + 100원 (총 4개) <br>
 최적의 방법: 800원 = 400원 + 400원 (총 2개)


##### 3) 큰 수의 법칙: 배열의 특정한 인덱스에 해당하는 수가 연속해서 K번을 초과하여 더해질 수 없는 것
 예1) [2, 4, 5, 4, 6]이라는 배열이 있고, M = 8, K = 3일때,  <br>
 8개의 숫자를 더하고, 특정한 인덱스의 수가 연속해서 3번까지만 더해질 수 있으므로, <br>
 최적의 방법: 6+6+6+5+ 6+6+6+5 = 46
       
 예2) [3, 4, 3, 4, 3]이라는 배열이 있고, M = 7, K = 2일때,  <br>
 7개의 숫자를 더하고, 특정한 인덱스의 수가 연속해서 2번까지만 더해질 수 있으므로, <br>
 최적의 방법: 4+4+ 4+4+ 4+4+ 4 = 28 (인덱스가 다른 4를 2번씩 더함)
 
 
```python
# Q2) 큰 수의 법칙

# n, m, k를 공백으로 구분하여 입력받기
n, m, k = map(int, input('').split())

# N개의 수를 공백으로 구분하여 입력받기
data = list(map(int, input('').split())) # 위 방법에서, list()만 붙여주면 됨

data.sort() # 리스트 정렬하기

```
   
```python
# Q3) 숫자 카드 게임: n x m 형태의 카드에서 각 행의 가장 작은 값 중 가장 큰 값을 찾아야함

# NxM 행렬일 때, 각 행을 따로 입력 받을 수 있음
for i in range(n):
     data = map(int, input('%d행을 입력하시오: '%(i+1)).split()) # 각 행의 m개의 데이터 입력

# min(리스트이름), max(리스트이름)으로 리스트에서 최솟값, 최댓값 찾기
row.append(min(data)) # data라는 리스트의 최솟값을 row라는 리스트에 추가함

# min(비교할 정수들), max(비교할 정수들) 로 최솟값 최댓값 찾기
result = max(result, min(data)) # result라는 정수와 min(data)라는 정수를 비교해, 더 큰값을 result에 넣음

```

```python
# Q4) 1이 될 때까지

# 무한 반복을 위해 while True 사용
while True:
    if n == 1:
        break

    elif n%k != 0:
        n -= 1
        count += 1

    else:
        n //= k
        count += 1

```

### ch4. 구현

``` python
# Q1) 상하좌우(L: 왼쪽으로 한 칸 이동, R: 오른쪽으로 한 칸 이동, U: 위로 한 칸 이동, D: 아래으로 한 칸 이동)
   
# 여행 계획 입력받기
plan = list(input('여행 계획: ').split())
   
# move_types와 dx, dy를 리스트로 만들어서, index가 같게 할 수 있음
move_types = ['L', 'R', 'U', 'D']
dx = [0, 0, -1, 1]
dy = [-1, 1, 0, 0]
for plan in plans:
    for i in range(len(move_types)):
        # 임시로 이동해본 좌표
        if plan == move_types[i]:
            temp_x = loc[0] + dx[i]
            temp_y = loc[1] + dy[i]
   
```


```python
# Q2) 시각

# 변수값이 int인지 string인지 확인 잘하기!!
result = int(n) # n을 정수로 바꿔줌
result = str(n) # n을 string으로 바꿔줌

# string을 append할 때, +기호 사용
time = str(i)+str(j)+str(k)

# string의 find함수를 이용해, 특정 string의 index값 혹은 존재 여부를 알 수 있음
if time.find('3') != -1: # time이라는 string에 '3'이라는 문자가 있으면 index값을 반환, 없으면 -1반환
    count += 1

# str
if '3' in str(i)+str(j)+str(k): # '3'이 str(i)+str(j)+str(k)에 있는지 확인
    count += 1
```
<br>

```python
# Q3) 왕실의 나이트

#ord함수로 ascii코드를 정수값으로
x = ord(loc[0])-ord('a')+1 # loc은 2자리 문자열

# 8가지 방향 정의 후, for문에서 사용
steps = [(-2,-1), (-2,1), (2,-1), (2,1), (-1,2), (-1,-2), (1,2),(1,-2)]
for step in steps:
    temp_x = x + step[0]
    temp_y = y + step[1]

```

```python
# Q5) 게임 개발!! (못풂..)

```

### ch5. DFS/BFS 
##### 1) DFS/BFS는 대표적인 탐색 알고리즘
##### 2) 스택(First in Last out), 큐(First in First out), 재귀함수 이해 필요 

```python
# 1. 스택: 리스트로 표현, First in last out
stack = []

# 삽입(7)
stack.append(7)

#삭제()
stack.pop()

```

```python
# 2. 큐: deque로 표현, First in First out
from collections import deque
queue = deque()

# 삽입(7)
queue.append(7)

#삭제
queue.popleft()
```

```python
# 3. 재귀 함수

def recursive_function(i):
    # 50번째 출력했을 때, 종료되도록 종료 조건 명시
    if i==3:
        return
    print(i,'번째 재귀 함수에서', i+1,'번째 재귀 함수를 호출합니다.')
    recursive_function(i+1)
    print(i, '번째 재귀 함수에서 재귀함수를 종료합니다.')

recursive_function(1)

# 실행결과:
# 1 번째 재귀 함수에서 2 번째 재귀 함수를 호출합니다.
# 2 번째 재귀 함수에서 3 번째 재귀 함수를 호출합니다.
# 2 번째 재귀 함수에서 재귀함수를 종료합니다.
# 1 번째 재귀 함수에서 재귀함수를 종료합니다.
```
```python
# 4. for문으로 구현한 n!
def factorial_iterative(n):
    result = 1
    # 1부터 n까지의 수를 차례대로 곱하기
    for i in range(1,n+1):
        result *= i
    return result


# 재귀함수로 구현한 n!
def factorial_recursive(n):
    if n <= 1: # n이 1 이하인 경우 1을 반환
        return 1
    return n * factorial_recursive(n-1)

# n! = n * (n-1)!
print('for문으로 구현:', factorial_iterative(5))
print('재귀함수로 구현:', factorial_recursive(5))
```

```python
# 5. 행(Row)이 3개인 2차원 리스트로 인접 리스트 표현
graph = [[] for _ in range(3)] # print(graph) 실행결과: [[], [], []]

# 노드 0에 연결된 노드 정보 저장(노드, 거리)
graph[0].append((1,7)) # 0노드와 1노드가 연결, 거리는 7
graph[0].append((2,5)) # 0노드와 2노드가 연결, 거리는 5

# 노드 1에 연결된 노드 정보 저장(노드, 거리)
graph[1].append((0,7)) # 1노드와 0노드가 연결, 거리는 7

# 노드 2에 연결된 노드 정보 저장(노드, 거리)
graph[2].append((0,5)) # 2노드와 0노드가 연결, 거리는 5


print(graph)

# 실행 결과: [[(1, 7), (2, 5)], [(0, 7)], [(0, 5)]]
```

### ch6. 정렬

### ch7. 이진 탐색

### ch8. 다이나믹 프로그래밍

### ch9. 최단 경로

### ch10. 그래프 이론

