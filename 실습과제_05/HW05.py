import math

map = [ ['1', '1', '1', '0', '1', '1', '1', '1', '1', '1'],
        ['e', '0', '0', '0', '0', '0', '0', '0', '0', '0'],
        ['1', '1', '1', '1', '0', '1', '0', '1', '1', '1'],
        ['1', '1', '0', '1', '0', '1', '1', '1', '0', '1'],
        ['1', '1', '0', '1', '0', '1', '0', '0', '0', '1'],
        ['0', '0', '0', '0', '0', '0', '0', '1', '0', '1'],
        ['1', '0', '1', '1', '0', '1', '1', '1', '0', '0'],
        ['1', '1', '0', '0', '0', '0', '0', '0', '0', '1'],
        ['1', '1', '0', '1', '0', '1', '0', '1', '0', 'x'],
        ['0', '0', '0', '1', '1', '1', '0', '1', '1', '1']]
MAZE_SIZE = 10

# 갈 수 있는 방인지 검사
def isValidPos(x,y) :
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE :
        return False
    else :
        return map[y][x] == '0' or map[y][x] == 'x'

# 스택 클래스
class Stack:
    def __init__(self):
        self.top = []
    
    def isEmpty(self): 
        return len(self.top ) == 0
    
    def push(self, item) :
        self.top.append(item)

    def peek(self):
        if not self.isEmpty():
            return self.top[-1]
    
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
        
    def size(self):
        return len(self.top)
    
    def clear(self):
        self.top = []    


# 스택_깊이우선탐색 함수
def DFS():
    stack = Stack()
    stack.push((0,1))
    print('DFS: ')

    while not stack.isEmpty():    # 공백이 아닐동안
        here = stack.pop()      # 꺼낸 항목
        print(here, end = '->')
        (x, y) = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'     # 현재위치 지나옴 표시.
            # 상하좌우 검사, 갈 수 있으면 삽입
            if isValidPos(x, y-1): stack.push((x, y-1))  # 상
            if isValidPos(x, y+1): stack.push((x, y+1))  # 하
            if isValidPos(x-1, y): stack.push((x-1, y))  # 좌
            if isValidPos(x+1, y): stack.push((x+1, y))  # 우
        print('현재스택: ', stack.top)
    return False
    
result = DFS()
if result : print('미로탐색 성공!')
else : print('미로탐색 실패')