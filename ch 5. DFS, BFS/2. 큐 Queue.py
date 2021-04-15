# 2. 큐 예제
from collections import deque
queue = deque()


# 삽입(7) - 삽입(6) - 삽입(10) - 삽입(3) - 삽입(5) - 삭제() - 삽입(2) - 삽입(8) - 삭제()
queue.append(7)
queue.append(6)
queue.append(10)
queue.append(3)
queue.append(5)

queue.popleft()

queue.append(2)
queue.append(8)

queue.popleft()

print(queue) # 순서대로 출력

queue.reverse() # 역순으로 출력
print(queue)