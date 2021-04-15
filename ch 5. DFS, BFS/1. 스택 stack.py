# 1. 스택 예제
stack = []

# 삽입(7) - 삽입(6) - 삽입(10) - 삽입(3) - 삽입(5) - 삭제() - 삽입(2) - 삽입(8) - 삭제()

stack.append(7)
stack.append(6)
stack.append(10)
stack.append(3)
stack.append(5)

stack.pop()

stack.append(2)
stack.append(8)

stack.pop()

print(stack) # 차례대로 출력
print(stack[::-1]) # 뒤에서부터 출력