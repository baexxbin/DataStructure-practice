class BSTNode:                          # 이진탐색트리를 위한 노드 클래스
    def __init__(self, key, value):     # 생성자 : 키와 값을 받음     
        self.key = key                  # 키(key)
        self.value = value              # 값(key)
        self.left = None                # 왼쪽 자식에 대한 링크 
        self.right = None               # 오른쪽 자식에 대한 링크
    
def preorder(n):                                # 전위 순회(VLR)
    if n is not None:
        print(n.data, end=" ")                  # 먼저 루트노드 처리(화면 출력)
        preorder(n.left)                        # 왼쪽 서브트리 처리
        preorder(n.right)                       # 오른쪽 서브트리 처리

def inorder(n):                                 # 중위 순회 함수
    if n is not None:
        inorder(n.left)                         # 왼쪽 서브트리 처리    
        print(n.data, end = " ")                 # 루트 노드 처리
        inorder(n.right)                        # 오른쪽 서브트리 처리

def postorder(n):                               # 후위 순회 (LRV)
    if n is not None:                   
        postorder(n.left)                       # 왼쪽 서브트리 처리
        postorder(n.right)                      # 오른쪽 서브트리 처리
        print(n.data, end = " ")                # 루트 노드 처리

def levelorder(root):                           # level 순회
    queue = CircularQueue()                     # 큐 객체 초기화
    queue.enqueue(root)                         # 최초의 큐에는 루트 노드만 들어있음.
    while not queue.isEmpty():                  # 큐가 공백상태가 아닌 동안
        n = queue.dequeue()                     # 큐에서 맨 앞의 노드 n을 꺼냄
        if n is not None:
            print(n.data, end = " ")            # 먼저 노드의 정보를 출럭
            queue.enqueue(n.left)               # n의 왼쪽 자식 노드를 큐에 삽입
            queue.enqueue(n.right)              # n의 오른쪽 자식 노드를 큐에 삽입

def search_bst(n, key):                         # 탐색연산(순환함수)
    if n == None:
        return None
    elif key == n.key:                          # n의 키 값과 동일 => 탐색 성공
        return n
    elif key < n.key:                           # key < n의 키
        return search_bst(n.left, key)          # 순환호출로 왼쪽 서브트리 탐색
    else:                                       # key > n의 키
        return search_bst(n.right, key)         # 순환호출로 오른쪽 서브트리 탐색

def search_bst_iter(n, key):                    # 탐색연산(반복함수)
    while n != None:                            # n의 값이 None이 아닐 때 까지
        if key == n.key:            
            return n
        elif key < n.key:                       # key < n의 키
            n = n.left                          # n을 왼쪽 서브트리의 루트로 이동
        else:                                   # key > n의 키
            n = n.right                         # n을 오른쪽 서브트리의 루트로 이동
        return None                             # 찾는 키의 노드가 없음


def search_max_bst(n):
    while n != None and n.right != None:
        n = n.right
    return n

def search_min_bst(n):
    while n != None and n.left != None:
        n = n.left
    return n

def insert_bst(r, n):                           # 이진탐색트리 삽입연산
    if n.key < r.key:                           # 삽입할 노드의 키가 루트보다 작으면
        if r.left is None:                      # 루트의 왼쪽 자식이 없으면
            r.left = n                          # n은 루트의 왼쪽 자식이 됨.
            return True 
        else:                                   # 루트의 왼쪽 자식이 있으면
            return insert_bst(r.left, n)        # 왼쪽 자식에게 삽입하도록 함
    elif n.key > r.key:                         # 삽입할 노드의 키가 루트보다 크면        
        if r.right is None:                     # 루트의 오른쪽 자식이 없으면
            r.right = n                         # n은 루트의 오른쪽 자식이 됨
            return True                         
        else:                                   # 루트의 오른쪽 자식이 있으면
            return insert_bst(r.right, n)       # 오른쪽 자식에게 삽입하도록 함
    else:                                       # 키가 중복되면
        return False                            # 삽입하지 않음

def delete_bst_case1(parent, node, root):   # 단말 노드 삭제
    if parent is None:                      # 삭제할 단말 노드가 루트이면
        root = None                         # 공백 트리가 됨
    else:
        if parent.left == node:             # 삭제할 노드가 부모의 왼쪽 자식이면
            parent.left = None              # 부모의 왼쪽 링크를 None
        else:                               # 오른쪽 자식이면
            parent.right = None             # 부모의 오른쪽 링크를 None

    return root                             # root가 변경될 수도 있으므로 반환

def delete_bst_case2(parent, node, root):   # 자식이 하나인 노드 삭제
    if node.left is not None:               # 삭제할 노드가 왼쪽 자식만 가짐
        child = node.left                   # child는 왼쪽 자식
    else:                                   # 삭제할 노드가 오른쪽 자식만 가짐
        child = node.right                  # child는 오른쪽 자식

    if node == root:                        # 없애려는 노드가 루트이면
        root = child                        # 이제 child가 새로운 루트가 됨
    else:
        if node is parent.left:             # 삭제할 노드가 부모의 왼쪽 자식
            parent.left = child             # 부모의 왼쪽 링크를 변경
        else:                               # 삭제할 노드가 부모의 오른쪽 자식
            parent.right = child            # 부모의 오른쪽 링크를 변경

    return root

def delete_bst_case3(parent, node, root):     # 자식이 둘인 노드 삭제
    succp = node                    # 후계자의 부모 노드
    succ = node.right               # 후계자 노드
    while(succ.left != None):       # 후계자와 부모노드 탐색
        succp = succ
        succ = succ.left

    if(succp.left == succ):         # 후계자가 왼쪽 자식이면
        succp.left = succ.right     # 후계자의 오른쪽 자식 연결
    else:                           # 후계자가 오른쪽 자식이면
        succp.right = succ.right    # 후계자의 왼쪽 자식 연결

    node.key = succ.key             # 후계자의 키와 값을
    node.value = succ.value         # 삭제할 노드에 복사
    node = succ;                    # 실제로 삭제하는 것은 후계자 노드

    return root                     # 일관성을 위해 root 반환

def delete_bst(root, key):
    if root == None : return None                           # 공백 트리

    parent = None                                           # 삭제할 노드의 부모 탐색
    node = root                                             # 삭제할 노드 탐색
    while node != None and node.key != key:                 # parent 탐색
        parent = node
        if key < node.key : node = node.left
        else : node = node.right
        
    if node == None : return None                           # 삭제할 노드가 없음
    if node.left == None and node.right == None:            # case 1 : 단말 노드
        root = delete_bst_case1(parent, node, root)
    elif node.left == None or node.right == None:           # case 2 : 유일한 자식
        root = delete_bst_case2(parent, node, root)
    else:                                                   # case 3 : 두 개의 자식
        root = delete_bst_case3(parent, node, root)

    return root                                             # 변경된 루트 노드를 반환

class BSTMap():
    def __init__(self):
        self.root = None
    def isEmpty(self): return self.root == None
    def clear(self): self.root = None
    def size(self): return count_node(self.root)
    def search(self, key): return search_bst(self.root, key)
    def findMax(self): return search_max_bst(self.root)
    def findMin(self): return search_min_bst(self.root)
    def insert(self, key, value = None):
        n = BSTNode(key, value)
        if self.isEmpty():
            self.root = n
        else:
            insert_bst(self.root, n)
    def delete(self, key):
        self.root = delete_bst(self.root, key)
    def display(self, msg = "BSTMAP :"):
        print(msg, end = '')
        inorder(self.root)
        print()

def printBinarySearchTree():
    print("======== 이진탐색트리를 이용한 맵 테스트 ========\n")

    map = BSTMap()
    data = [35, 18, 7, 26, 12, 3, 68, 22, 30, 99]

    print("[삽입 연산] : ", data)
    for key in data:
        map.insert(key)

    map.display("[중위 순회] : ")

    if map.search(26) != None : print("[탐색 26] : 성공")
    else : print("[탐색 26] : 실패")
    if map.search(25) != None : print("[탐색 25] : 성공")
    else : print("[탐색 25] : 실패")

    map.delete(3);  map.display("[    3 삭제] : ")
    map.delete(68); map.display("[   68 삭제] : ")
    map.delete(18); map.display("[   18 삭제] : ")
    map.delete(35); map.display("[   35 삭제] : ")

printBinarySearchTree()