# 큐
MAX_QSIZE = 20
class CircularQueue:
    def __init__(self):
        self.front = 0
        self.rear = 0
        self.items = [None]*MAX_QSIZE

    def isEmpty(self): return self.front == self.rear
    def isFull(self): return self.front == (self.rear+1)%MAX_QSIZE
    def clear(self): self.front = self.rear

    def enqueue(self, item):
        if not self.isFull():
            self.rear = (self.rear+1) % MAX_QSIZE
            self.items[self.rear] = item

    def dequeue(self):
        if not self.isEmpty():
            self.front = (self.front+1) % MAX_QSIZE
            return self.items[self.front]
    
    def peek(self):
        if not self.isEmpty():
            return self.items[(self.front+1) % MAX_QSIZE]
    
    def size(self):
        return(self.rear - self.front + MAX_QSIZE) % MAX_QSIZE
    
    def display(self):
        out = []
        if self.front < self.rear:
            out = self.items[self.front+1 : self.rear+1]
        else:
            out = self.items[self.front+1 : MAX_QSIZE] + self.items[0:self.rear+1]
        print("[f=%s, r=%d] ==> " %(self.front, self.rear), out)

# 이진트리의 노드
class TNode:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

# 전위 순회 VLR
def preorder(n):
    if n is not None:
        print(n.data, end=' ') # 처리
        preorder(n.left)
        preorder(n.right)

# 중위 순회 LVR
def inorder(n):
    if n is not None:
        inorder(n.left)
        print(n.data, end=' ')
        inorder(n.right)
    
# 후위 순회 LRV
def postorder(n):
    if n is not None:
        postorder(n.left)
        postorder(n.right)
        print(n.data, end=' ')

# 레벨 순회
def levelorder(root):
    queue = CircularQueue()
    queue.enqueue(root)
    while not queue.isEmpty():
        n = queue.dequeue()
        if n is not None:
            print(n.data, end=' ')
            queue.enqueue(n.left)
            queue.enqueue(n.right)

    
# 노드 개수 구하기
def count_node(n):          # n을 루트로 하는 이진트리
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right) # 좌우서브트리 노드 수 + 루트 노드(1)

# 단말 노드 개수 구하기
def count_leaf(n):
    if n is None:                               # 공백트리
        return 0
    elif n.left is None and n.right is None:    # 좌우 둘중하나 없음
        return 1
    else:                                       # 비단말, 좌우 둘다존재, 자식수 합하기
        return count_leaf(n.left) + count_leaf(n.right)
    
# 트리의 높이 구하기
def calc_height(n):
    if n is None:
        return 0
    hLeft = calc_height(n.left)
    hRight = calc_height(n.right)
    if (hLeft > hRight):
        return hLeft + 1
    else:
        return hRight + 1

# 완전이진트리 검사
def is_complete_binary_tree(root):
    queue2 = CircularQueue()
    queue2.enqueue(root)
    check = False

    if root is None:                    # 루트가없으면 빈트리임으로 False
        return False
    
    while not queue2.isEmpty():           
        put = queue2.dequeue()
        if(put.left):                   # 왼쪽이 있을때 (1)
            if check == True:           # 왼쪽은 있는데 오른쪽은 없음
                return False            # 완전이진트리 아님
            queue2.enqueue(put.left)    # 왼쪽 큐에 넣기
        else:                           # 왼쪽이 없을때 (1)
            check = True                # 왼쪽하나 없으니까 check값 True로 바꿈
        
        if(put.right):                  # 오른쪽이 있을때 (1)
            if check == True:           # 오른쪽은 있는데 왼쪽은 없음
                return False            # 완전이진트리 아님
            queue2.enqueue(put.right)   # 오른쪽 큐에 넣기
        else:                           # 오른쪽이 없을때 (1)
            check = True                # 오른쪽 하나 없으니까 check값 True로 바꿈
    return True

# 임의의 노드 레벨구하기
def level(root, node):
    queue3 = CircularQueue()
    queue3.enqueue(root)

    if root is None:
        return False
    
    level = 1
    while not queue3.isEmpty():
        out = queue3.dequeue()

        if node == out:                 # 찾는노드가 루트노드일때
            return level

        if(out.left):                   # 왼쪽이 있을때
            level += 1                  # 레벨증가
            queue3.enqueue(out.left)    # 큐에 넣고
            if node == out.left:        # 찾는 노드이면
                return level            # 레벨 반환
        elif(out.right):                # 왼쪽이 없고 오른쪽은 있을때
            # level += 1
            queue3.enqueue(out.right)
            if node == out.right:
                return level

        if(out.right):                  # (왼쪽있고)오른쪽이 있을때 == 둘다있을때
            queue3.enqueue(out.right)
            if node == out.right:
                return level




# ======================================================================
g = TNode('G', None, None)
h = TNode('H', None, None)
d = TNode('D', None, None)
e = TNode('E', g, h)
f = TNode('F', None, None)
b = TNode('B', d, None)
c = TNode('C', e, f)
root = TNode('A', b, c)

print('In-Order: ', end='')
inorder(root)
print('\n')

print('Pre-Order: ', end='')
preorder(root)
print('\n')

print('Post-Order: ', end='')
postorder(root)
print('\n')

print('Level-Order: ', end='')
levelorder(root)
print('\n')

print(f'노드의 개수: {count_node(root)}개')
print("단말의 개수: %d개" %count_leaf(root))
print("트리의 높이: %d" %calc_height(root))


a = TNode('A', None, None)
b = TNode('B', None, None)
c = TNode('C', None, None)
d = TNode('D', None, None)
e = TNode('E', None, None)
sl = TNode('/', a, b)
st = TNode('*', sl, c)
st2 = TNode('*', st, d)
root2 = TNode('+', st2, e)

print('In-Order: ', end='')
inorder(root2)
print('\n')

print('Pre-Order: ', end='')
preorder(root2)
print('\n')

print('Post-Order: ', end='')
postorder(root2)
print('\n')

print('Level-Order: ', end='')
levelorder(root2)
print('\n')

print(f'노드의 개수: {count_node(root2)}개')
print("단말의 개수: %d개" %count_leaf(root2))
print("트리의 높이: %d" %calc_height(root2))

#============================= P8.2 =================================
c = TNode('C', None, None)
d = TNode('D', None, None)
f = TNode('F', None, None)
b = TNode('B', c, d)
e = TNode('E', None, f)
root3 = TNode('A', b, e)

result = is_complete_binary_tree(root3)
print()
if result == True: print('완전이진트리')
else: print('완전이진트리 아님')

print()
lev = level(root3, d)
print(f'd의 레벨은 {lev}입니다.')






