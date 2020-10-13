# Python list를 이용한 Sparse Polynomial 클래스 구현
# Linked List.
class Node:                                 # 노드 클래스 선언
    def __init__(self, elem, next = None):  # 생성자
        self.data = elem                    # 데이터 변수 저장
        self.link = next                    # 다음 노드의 위치 확인

class LinkedList:                           # 연결된 리스트 클래스
    def __init__(self):                     # 생성자
        self.head = None
    
    def isEmpty(self):                      # 헤드가 가리키는 부분이 None이라면 비어있는 리스트
        return self.head == None
    
    def clear(self): self.head = None       # 헤드가 가라키는 부분을 None으로 하여 비운 리스트

    def size(self):                         # 리시트의 크기를 확인하는 함수
        node = self.head                    # Head의 위치를 node에 넣어준다.
        count = 0;                          # node가 비어있다면 count는 0
        while node is not None:             # node가 비어있지않다면
            node = node.link                # node는 다음 node의 위치를 저장
            count += 1                      # count는 1 상승
        return count                        # 모든 요소에 대한 검사가 끝났다면 count 반환

    def getNode(self,pos):                  # pos번째 Node를 반환하는 함수
        if pos < 0 : return None            # pos가 음수라면 None을 반환
        node = self.head                    # 아니라면 node에 head를 저장 / head부터 시작
        while pos> 0 and node != None :     # pos가 양수이고 node가 None이 아니라면 / pos번 반복
            node = node.link                # node는 다음 node의 위치를 저장 / 다음 노드로 이동
            pos -= 1                        # pos는 1 감소
        return node                         # 최종 node 반환

    def getEntry(self, pos):                # pos번째 노드의 데이터 반환
        node = self.getNode(pos)            # pos번째 노드
        if node == None : return None       # 찾는 노드가 없다면 None return
        else : return node.data             # 그 노드의 데이터 필드 반환

    def replace(self, pos, elem):           # pos번째 노드의 데이터를 변경
        node = self.getNode(pos)            # pos번째 노드를 찾아
        if node != None:                    
            node.data = elem                # 데이터 필드에 elem 복사
    
    def find(self, data):                   # 데이터로 data를 갖는 노드 반환
        node = self.head                    # head부터 시작
        while node is not None:             # 모든 노드에서 찾음
            if node.data == data :          # 찾아지면 바로 반환
                return node                 
            node = node.link                
        return node                         # 찾아지지 않으면 None 반환
    
    def insert(self, pos, elem):            
        before = self.getNode(pos-1)        # before 노드를 찾음
        if before == None :                 # 맨 앞에 삽입하는 경우
            self.head = Node(elem, self.head)
        else :                              # 중간에 앞에 삽입하는 경우
            node = Node(elem, before.link)  # 노드 생성 + 다음 노드와 연결
            before.link = node              # 앞의 노드와 추가된 노드 연결

    def delete(self, pos):                      
        before = self.getNode(pos-1)        # before 노드를 찾음
        if before == None:                  # 맨 앞 노드를 삭제
            if self.head is not None:       # 공백이 아니면
                self.head = self.head.link  # head를 다음으로 이동
            elif before.link != None :      # 중간에 있는 노드 삭제
                before.link = before.link.link # before의 link가 삭제할 노드의 다음 노드를 가리키도록 함.

# 하나의 항을 나타내기 위한 클래스
class Term:
    def __init__(self, expon, coeff):       # 생성자
        self.expon = expon                  # 지수
        self.coeff = coeff                  # 계수

# 희소 다항식 클래스
class SparsePoly(LinkedList):               # LinkedList 클래스 상속
    def __init__(self):                     # 생성자
        super().__init__()                  # 상속
    
    def degree(self) :                      # 차수를 반환하는 함수
        if self.head == None :return 0
        else : return self.head.data.expon  # 차수 값 접근 법 

    def display(self, msg = "f(x) = "):     # 다항식을 출력하는 함수
        print(msg, end = "")
        node = self.head                    # node를 head로 저장
        while not node == None:             # 모든 항목에 대해서
            print(node.data.coeff, "x^%d" % node.data.expon, end = ' + ')
            node = node.link                # 다음 노드로 연결
        print()

    def read(self):
        self.clear()                        # 연결리스트 초기화
        token = input("다항식 입력(지수 계수 지수 계수 ... [엔터]) : ").split(" ")  # 입력
        for i in range (len(token) // 2):   # token내에 2개의 수가 계수와 지수를 나타내기에 2로 나누어 전체 길이를 확인한다.
            self.insert(self.size(), Term(int(token[i*2+1]), float(token[i*2])))
                                            # Term의 항을 나타내는 클래스의 변수에 지수는 int형으로 계수는 float형으로 나타낸다. 
    
    def add(self, B):                       # 다항식의 덧셈 연산
        c = SparsePoly()                    # 다항식 클래스를 대입
        a = self.head                       # head 값을 저장한다.
        b = B.head                          # head 값을 저장한다.
        while not a == None and not b == None: # 모든 항목에 대하여
            if (a.data.expon == b.data.expon): # 지수가 같다면
                c.insert(c.size(), Term(a.data.expon, a.data.coeff + b.data.coeff)) # 다항식 클래스 c에 지수와 더한 계수 값을 대입하였다.
                a = a.link                  # 다음 노드로 이동
                b = b.link                  # 다음 노드로 이동
            elif (a.data.expon > b.data.expon): # a의 지수가 더 크다면
                c.insert(c.size(), Term(a.data.expon, a.data.coeff))
                                            # a의 지수와 계수를 대입
                a = a.link                  # 다음 노드로 이동
            else:                           # b의 지수가 더 크다면
                c.insert(c.size(), Term(b.data.expon, b.data.coeff))
                                            # b의 지수와 계수를 대입
                b = b.link                  # 다음 노드로 이동
        while not a == None : # 나머지 연산이 되지 않은 부분을 검사하여 나머지 항들에 대한 연산 시행                
            c.insert(c.size(), Term(a.data.expon, a.data.coeff))
            a = a.link
        while not b == None : 
            c.insert(c.size(), Term(b.data.expon, b.data.coeff))
            b = b.link
        return c

    def neg(self):                          # 모든 계수에 -1을 곱하는 함수
        neg_class = SparsePoly()            # 값을 저장할 클래스 저장
        node = self.head                    # head 저장
        while not node == None:             # 모든 항목에 대하여
            neg_class.insert(neg_class.size(), Term(node.data.expon, node.data.coeff * -1)) # 계수에 -1을 곱한 값을 insert한다.
            node = node.link                # 다음 노드로 이동
        return neg_class

    def mult(self, B):                      # 다항식의 곱셈
        e = SparsePoly()                    # 다항식 클래스를 대입
        a = self.head                       # head 값을 저장한다.
        # 다항식의 곱셈 알고리즘
        while not a == None:
            b = B.head                      # head 값을 저장한다.
            while not b == None:
                mul = SparsePoly()          # 각각의 항을 곱셈한 값을 저장할 클래스
                mul.insert(mul.size(), Term(a.data.expon * b.data.expon, a.data.coeff * b.data.coeff))
                e = e.add(mul)              # 같은 지수의 항들의 계수의 덧셈
                b = b.link                  # 다음 노드로 이동
            a = a.link                      # 다음 노드로 이동
        return e

    def sub(self, B):
        d = a.add(B.neg())                  # B 희소 다항식의 계수에 -1을 곱한 후 a의 다항식과 덧셈 연산
        return d

# ---------------------------------------------------------------------------------------------------

# 희소 다항식 객체 생성
a = SparsePoly()
b = SparsePoly()

# 희소 다항식 입력
a.read()
b.read()

# 다항식의 연산 (덧셈, 뺄셈, 곱셈)
c = a.add(b)
d = a.sub(b)
e = a.mult(b)

# 각각의 식 출력
a.display("A = ")
b.display("B = ")
c.display("A + B = ")
d.display("A - B = ")
e.display("A * B = ")