# Term 클래스 //데이터E로 들어갈값(지수, 계수)
class Term :
    def __init__(self, expon, coef):
        self.expon = expon  # 지수
        self.coef = coef    # 계수

# Node 클래스
class Node :
    def __init__ (self, elem, link = None):
        self.data = elem
        self.link = link

# LinkedList 클래스
class LinkedList :
    def __init__(self):
        self.head =None
    
    # 기본 함수
    def isEmpty(self): return self.head == None     # 공백상태 검사
    def clear(self): self.head = None   # 리스트 초기화
    def size(self):     # 리스트의 크기
        node = self.head
        count = 0
        while not node == None :
            node = node.link
            count += 1
        return count

    def display(self, msg):     # 리스트 출력
        print(msg, end='')
        node = self.head
        while not node == None :
            print(node.data, end='')
            node = node.link
        print()
    
    # pos번째 노드 반환함수
    def getNode(self, pos):
        if pos < 0 : return None
        node = self.head;
        while pos > 0 and node != None :
            node = node.link
            pos -= 1
        return node

    # pos의 데이터만 반환 함수
    def getEntry(self, pos):
        node = self.getNode(pos)
        if node == None : return None
        else : return node.data

    def replace(self, pos, elem):
        node = self.getNode(pos)
        if node != None: node.data = elem

    # 원하는 데이터를 가진 노드 찾는 함수
    def find(self, elem) :
        node = self.head;
        while node is not None:
            if node.data.expon == elem : return node
            node = node.link
        return node

    # 삽입 연산
    def insert(self, pos, elem) :
        before = self.getNode(pos-1)
        if before == None :
            self.head = Node(elem, self.head)
        else :
            node = Node(elem, before.link)
            before.link = node

    # 삭제 연산 
    def delete(self, pos) :
        before = self.getNode(pos-1)
        if before == None:
            if self.head is not None:
                self.head = self.head.link
        elif before.link != None:
            before.link = before.link.link


# SparsePoly 클래스 // 매개변수로 LinkedList 상속
class SparsePoly(LinkedList) :
    def __init__(self):
        super().__init__()

    # degree 최고차수
    def degree(self):
        if self.head == None: return 0
        else: return self.head.data.expon


    # read 항 입력받기
    def read(self):
        self.clear()
        token = input("입력: 계수, 지수 [엔터]: ").split(" ")                       # 값 입력 받기
        for i in range (len(token)//2):                                             # 계수, 지수가 한 쌍임으로 //2
            self.insert(self.size(), Term(int(token[i*2+1]), float(token[i*2])))    # 현재 리스트의 길이번째, 계수와 지수 넣어주기

            
    # display 입력받은 항 출력
    def display(self, msg=""):
        print(msg, end='')
        node = self.head    # 노드연결

        while not (node == None) :      # 노드가 비어있지 않으면 루프
            print(" %dx^%d " %(node.data.coef, node.data.expon), end='')
            if not (node.link == None): # 마지막 노드가 아닐때 + 붙여주기
                print("+", end='')
            node = node.link            # 다음 노드로 이동
        print()    

    # sub 더하기
    def add(self, B):
        add_p = SparsePoly()    # 덧셈 저장할 객체생성

        node = self.head    # 노드연결
        b_node = B.head     # b노드 연결
        while not node == None and not b_node == None:    # 노드와 b노드가 None이 아닐때 까지
            if (node.data.expon == b_node.data.expon):    # 같은 계수이면 더하기
                add_p.insert(add_p.size(), Term(node.data.expon, node.data.coef + b_node.data.coef))
                node = node.link        # 다음노돌 이동
                b_node = b_node.link    # 다음 b노드로 이동
            elif (node.data.expon > b_node.data.expon):   # 노드가 크면 노드만 넣기
                add_p.insert(add_p.size(), Term(node.data.expon, node.data.coef))
                node = node.link        # 노드만 다음으로 이동
            elif (node.data.expon < b_node.data.expon):   # b노드가 크면 b노드만 넣기
                add_p.insert(add_p.size(), Term(b_node.data.expon, b_node.data.coef))
                b_node = b_node.link    # b노드만 다음으로 이동
        
        while not node == None:         # 위의 반복문 예외처리 (위 조건에서 하나만 fals여도 반복문 탈출됨)
            add_p.insert(add_p.size(), Term(node.data.expon, node.data.coef))
            node = node.link
        while not b_node == None:       # 위의 반복문 예외처리 (b노드의 값이 남았을때)
            add_p.insert(add_p.size(), Term(b_node.data.expon, b_node.data.coef))
            b_node = b_node.link
        return add_p


    # neg 빼기  
    def neg(self):
        neg_p = SparsePoly()    # neg한값 저장할 객체 생성
        n_node = self.head      # 노드 연결
        while not n_node == None:   # 노드가 끝이 아닐동안 반복
            neg_p.insert(neg_p.size(), Term(n_node.data.expon, -(n_node.data.coef)))    # 계수값에 - 붙여주기
            n_node = n_node.link    # 다음 노드로 이동
        return neg_p                # neg값 반환

    # sub 빼기
    def sub(self, B):
        sub_p = SparsePoly()
        sub_p = self.add(B.neg())   # neg한 B값과 더하기
        return sub_p

    # mult 곱하기
    def mult(self, B):
        mult_p = SparsePoly()   # 곱셈 리스트 객체생성
        node = self.head        # head로 노드연결
        
        while not node == None: # node의 끝이 아닐때까지 루프
            b_node = B.head     # head로 b노드 연결
            while not b_node == None:   # b노드가 끝이 아닐때 까지 루프
                temp = SparsePoly() # 루프당 곱한값을 잠시 넣어둘 리스트
                temp.insert(mult_p.size(), Term((node.data.expon + b_node.data.expon),(node.data.coef * b_node.data.coef))) # 곱셈실행
                mult_p = mult_p.add(temp)   # 같은항끼리는 더해주며 값 쌓기
                b_node = b_node.link        # 다음 b노드로 이동
            node = node.link                # 다음 노드로 이동
        return mult_p                       # 곱셈값 반환
        

# ================================= 실행공간 ==================================

# a,b객체 생성
a = SparsePoly()
b = SparsePoly()

# a,b값 받아드리기
a.read()
b.read()

# 연산 [덧셈, 뺄셈, 곱셈]
c = a.add(b)
d = a.sub(b) 
e = a.mult(b)

# 값 출력
a.display("A = ")
b.display("B = ")
c.display("A + B = ")
d.display("A - B = ")
e.display("A * B = ")


