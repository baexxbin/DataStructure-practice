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

# 이진탐색트리 노드
class BSTNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.left = None
        self.right = None

# 탐색연산
def search_bst(n, key):
    if n == None: return None
    elif key == n.key: return n
    elif key < n.key: return search_bst(n.left, key)
    else: return search_bst(n.right, key)

# 값을 이용한 탐색
def search_value_bst(n, value):
    if n == None: return None
    elif value == n.value: return n
    res = search_value_bst(n.left, value)
    if res is not None:
        return res
    else:
        return search_value_bst(n.right, value)

def search_max_bst(n):
    while n != None and n.right !=None:
        n = n.right
        return n

def search_min_bst(n):
    while n != None and n.left !=None:
        n = n.left
        return n

# 노드 개수 구하기
def count_node(n):          # n을 루트로 하는 이진트리
    if n is None:
        return 0
    else:
        return 1 + count_node(n.left) + count_node(n.right) # 좌우서브트리 노드 수 + 루트 노드(1)

# 탐색연산(순환함수)
def search_bst(n, key):                         
    if n == None:
        return None
    elif key == n.key:          # 찾는 키값이면 현재노드반환                    
        return n
    elif key < n.key:           # 찾는 키가 더 작은 값이라면 왼쪽 탐색                 
        return search_bst(n.left, key)          
    else:                       # 찾는 키가 더 큰 값이라면 오른쪽 탐색              
        return search_bst(n.right, key)

# 탐색연산(반복함수)
def search_bst_iter(n, key):                   
    while n != None:            # n이 None이 아닐때까지                  
        if key == n.key:        # 찾는값이면 n반환
            return n
        elif key < n.key:      # 찾는키가 더 작으면                 
            n = n.left         # 왼쪽탐색                  
        else:                  # 찾는키가 더 크면                 
            n = n.right        # 오른쪽 탐색                
        return None 

# 전위 순회(VLR)
def preorder(n):                                
    if n is not None:
        print(n.key, end=" ")                 
        preorder(n.left)                       
        preorder(n.right)                     

# 중위 순회 함수
def inorder(n):                                 
    if n is not None:
        inorder(n.left)                         
        print(n.key, end = " ")           
        inorder(n.right)                  

# 후위 순회 (LRV)
def postorder(n):                               
    if n is not None:                   
        postorder(n.left)                       
        postorder(n.right)                    
        print(n.key, end = " ")          

# level 순회
def levelorder(root):                          
    queue = CircularQueue()                    
    queue.enqueue(root)                        
    while not queue.isEmpty():                  
        n = queue.dequeue()                    
        if n is not None:
            print(n.data, end = " ")            
            queue.enqueue(n.left)             
            queue.enqueue(n.right)

# 삽입연산
def insert_bst(r, n):                           
    if n.key < r.key:                           
        if r.left is None:                      
            r.left = n                         
            return True 
        else:                                   
            return insert_bst(r.left, n)       
    elif n.key > r.key:                               
        if r.right is None:                   
            r.right = n                       
            return True                         
        else:                            
            return insert_bst(r.right, n)       
    else:                                      
        return False

# 단말노드 삭제
def delete_bst_case1(parent, node, root):   
    if parent is None:                      
        root = None                         
    else:
        if parent.left == node:            
            parent.left = None              
        else:                              
            parent.right = None        

    return root

# 자식하나 노드 삭제
def delete_bst_case2(parent, node, root):   
    if node.left is not None:               
        child = node.left                   
    else:                                   
        child = node.right              

    if node == root:                       
        root = child                       
    else:
        if node is parent.left:             
            parent.left = child            
        else:                             
            parent.right = child          

    return root

# 자식둘 노드 삭제
def delete_bst_case3(parent, node, root):     
    succp = node                    
    succ = node.right               
    while(succ.left != None):       
        succp = succ
        succ = succ.left

    if(succp.left == succ):        
        succp.left = succ.right     
    else:                           
        succp.right = succ.right    

    node.key = succ.key            
    node.value = succ.value     
    node = succ;             

    return root 

# 모든경우 삭제연산
def delete_bst(root, key):
    if root == None : return None                           
    # 삭제할 노드의 부모탐색
    parent = None                                       # 삭제할 부모의 노드, 일단 None값으로
    node = root                                          
    while node != None and node.key != key:             # 노드가 None이 아니고 키값을 찾기전까지 반복 
        parent = node                                   # 부모 찾음
        if key < node.key : node = node.left            # 키가 작으면 왼쪽
        else : node = node.right                        # 크면 오른쪽
        
    if node == None : return None                       # 삭제할 노드가 없음
    if node.left == None and node.right == None:        # 단말노드
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None:       # 자식하나
        root = delete_bst_case2(parent, node, root)
    else:                                               # 자식 둘
        root = delete_bst_case3(parent, node, root)

    return root                                         # 변경된 root노드 반환


# 이진탐색트리 맵
class BSTMap():
    def __init__ (self):
        self.root = None        # 트리의 루트노드 (루트를 가리킬 변수)
    
    def isEmpty(self): return self.root == None
    def clear(self): self.root = None
    def size(self): return count_node(self.root)
    def search(self, key): return search_bst(self.root, key)
    def searchValue(self, key): return search_value_bst(self.root, key)
    def findMax(self): return search_max_bst(self.root)
    def findMin(self): return search_min_bst(self.root)

    # 삽입연산
    def insert(self, key, value=None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)
    
    # 삭제연산
    def delete(self, key):
        self.root = delete_bst(self.root, key)

    # 출력
    def display(self, msg = "BSTMAP :"):
        print(msg, end = '')
        inorder(self.root)
        print()

#=======================================================
map = BSTMap()
data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]

print("[삽입연산] : ", data)
for key in data:
    map.insert(key)
map.display("[중위순회] : ")
if map.search(26) != None: print('[탐색 26] : 성공')
else: print('[탐색 26] : 실패')
if map.search(25) != None: print('[탐색 25] : 성공')
else: print('[탐색 25] : 실패')

map.delete(3);      map.display("[  3삭제] : ")
map.delete(68);      map.display("[  68삭제] : ")
map.delete(18);      map.display("[  18삭제] : ")
map.delete(35);      map.display("[  35삭제] : ")
