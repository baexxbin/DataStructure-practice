import queue
import math

map = [ ['1', '1', '1', '1', '1', '1'],
        ['e', '0', '1', '0', '0', '1'],
        ['1', '0', '0', '0', '1', '1'],
        ['1', '0', '1', '0', '1', '1'],
        ['1', '0', '1', '0', '0', 'x'],
        ['1', '1', '1', '1', '1', '1']]
MAZE_SIZE = 6

# 갈 수 있는 방인지 검사
def isValidPos(x,y) :
    if x < 0 or y < 0 or x >= MAZE_SIZE or y >= MAZE_SIZE :
        return False
    else :
        return map[y][x] == '0' or map[y][x] == 'x'

# 스택_깊이우선탐색 함수
def DFS():
    stack = queue.LifoQueue(maxsize=10)
    stack.put((0,1))
    print('DFS: ')

    while not stack.empty():    # 공백이 아닐동안
        here = stack.get()      # 꺼낸 항목
        print(here, end = '->')
        (x, y) = here
        if (map[y][x] == 'x'):
            return True
        else:
            map[y][x] = '.'     # 현재위치 지나옴 표시.
            # 상하좌우 검사, 갈 수 있으면 삽입
            if isValidPos(x, y-1): stack.put((x, y-1))  # 상
            if isValidPos(x, y+1): stack.put((x, y+1))  # 하
            if isValidPos(x-1, y): stack.put((x-1, y))  # 좌
            if isValidPos(x+1, y): stack.put((x+1, y))  # 우
        print('현재스택: ', stack)
    return False
    
result = DFS()
if result : print('미로탐색 성공!')
else : print('미로탐색 실패')


# 큐_너비우선탐색 함수
def BFS():
    que = queue.Queue(maxsize=10)
    que.put((0,1))
    print('BFS: ')

    while not que.empty():
        here = que.get()
        print(here, end='->')
        x,y = here
        if(map[y][x] == 'x') :
            return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1): que.put((x, y-1))  # 상
            if isValidPos(x, y+1): que.put((x, y+1))  # 하
            if isValidPos(x-1, y): que.put((x-1, y))  # 좌
            if isValidPos(x+1, y): que.put((x+1, y))  # 우

    return False

result2 = BFS()
if result2: print('미로탐색 성공!')
else: print('미로탐색 실패')

# 우선순위 큐 클래스
class PriorityQueue:
    def __init__(self):
        self.items = []
    
    def isEmpty(self):
        return len(self.items) == 0
    def size(self): return len(self.items)
    def enqueue(self, item):
        self.items.append(item)
    
    # 우선순위 항목 찾기
    def findMaxIndex(self):
        if self.isEmpty(): return None
        else:
            highest = 0
            for i in range(1, self.size()):
                if self.items[i][2] > self.items[highest][2]:
                    highest = i
            return highest

    def dequeue(self):
        highest = self.findMaxIndex()
        if highest is not None :
            return self.items.pop(highest)
    def peek(self):
        highest = self.findMaxIndex()
        if highest is not None :
            return self.items[highest]

(ox, oy) = (5, 4)
def dist(x,y):
    (dx,dy) = (ox-x, oy-y)
    return math.sqrt(dx*dx + dy*dy)

# 우선순위 큐_미로찾기
def MySearch():
    q = PriorityQueue()
    q.enqueue((0, 1, -dist(0,1)))
    print('PQueue: ')

    while not q.isEmpty():
        here = q.dequeue()
        print(here[0:2], end='->')
        x,y,_ = here
        if(map[y][x] == 'x') : return True
        else:
            map[y][x] = '.'
            if isValidPos(x, y-1) : q.enqueue((x, y-1, -dist(x,y-1)))
            if isValidPos(x, y+1) : q.enqueue((x, y+1, -dist(x,y+1)))
            if isValidPos(x-1, y) : q.enqueue((x-1, y, -dist(x-1,y)))
            if isValidPos(x+1, y) : q.enqueue((x+1, y, -dist(x+1,y)))
        print('우선순위 큐: ', q.items)
    return False

result3 = MySearch()
if result3: print('미로탐색 성공!')
else: print('미로탐색 실패')