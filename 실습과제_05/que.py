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

# 큐 클래스
MAX_QSIZE = 30
class Queue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None] * MAX_QSIZE
    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear + 1) % MAX_QSIZE
    
    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1)%MAX_QSIZE
            self.items[self.rear] = item
    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1)%MAX_QSIZE
            return self.items[self.front]
    def size(self):
        return (self.rear - self.front + MAX_QSIZE)%MAX_QSIZE
    
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1: self.rear+1]
        else:
            out = self.items[self.front+1:MAX_QSIZE] + self.items[0:self.rear+1]
        print("[f=%s, r=%d] ==> " %(self.front, self.rear), out)

# 큐_너비우선탐색 함수
def BFS():
    que = Queue()
    que.enqueue((0,1))
    print('BFS: ')

    while not que.isEmpty():
        here = que.dequeue()
        print(here, end='->')
        x,y = here
        if(map[y][x] == 'x') :
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1): que.enqueue((x, y-1))  # 상
            if isValidPos(x, y+1): que.enqueue((x, y+1))  # 하
            if isValidPos(x-1, y): que.enqueue((x-1, y))  # 좌
            if isValidPos(x+1, y): que.enqueue((x+1, y))  # 우
        print('현재큐: ', que.items)
    return False

result2 = BFS()
if result2: print('미로탐색 성공!')
else: print('미로탐색 실패')
