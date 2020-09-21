class Polynomial:
    def __init__(self):
        self.coef= []
        self.leng = len(self.coef) # 배열의 길이 = 최고차항의 값

    #  다항식의 차수 반환
    def degree(self):
        deg = self.leng - 1   # coef 계수의미, 0차(상수항)부터 시작함으로 -1
        return deg

    #  현재다항식 출력
    def display(self, msg ="f(x) = "):
        print_str = ''
        for i in range(len(self.coef)-1, -1, -1):
            if i == 0: 
                print_str += "%d" % self.coef[i]
            else:
                print_str += "%dx^%d + " % (self.coef[i],i)
        print(msg, print_str)

    # 다항식의 덧셈
    def add(self, b):
        add_p = Polynomial() # 덧셈다항식 객체생성
        if len(self.coef) > len(b.coef):
            add_p.coef = list(self.coef)    # 큰배열 만큼저장
        else:
            add_p.coef = list(b.coef)
        min_range = min(len(self.coef), len(b.coef))
        for i in range(min_range):
            add_p.coef[i] = self.coef[i] + b.coef[i]
        return add_p

    # neg 메소드
    def neg(self):
        neg_p = Polynomial()
        neg_p.coef = list(self.coef)
        for i in range(len(neg_p.coef)):
            neg_p.coef[i] *= -1
        return neg_p

    # 다항식의 뺄셈
    def sub(self, b):
        sub_p = Polynomial()    # 뺄셈객체 생성
        sub_p = self.add(b.neg())
        return sub_p
        
    # 다항식 곱셈
    def mul(self, b):
        mul_p = Polynomial()
        deg_self = len(self.coef)-1
        deg_b = len(b.coef)-1
        mul_p_deg = deg_self + deg_b
        
        # mul_p객체의 다항식 리스트에 항의 개수만큼 '0'을 삽입하여 리스트의 크기를 맞춤.
        for i in range(mul_p_deg + 1):
            mul_p.coef.append(0)

        for i in range(deg_self+1):
            for j in range(deg_b+1):
                mul_p.coef[i+j] += self.coef[i] * b.coef[j]
        return mul_p

    # x대입 계산결과 반환
    def eval(self, x):
        result = 0
        for i in range(len(self.coef)):
            result += self.coef[i]*(x ** i)
        return result
             
    
    # 다항식 입력
    def read(self):
        deg = int(input("다항식의 최고 차수를 입력하시오: "))
        for n in range(deg+1):
            coef = float(input( "\tx^%d의 계수 : " %(deg-n)))
            self.coef.append(coef)
        self.coef.reverse()

a = Polynomial()
b = Polynomial()

# 두 다항식 입력받기
a.read()
b.read()

# eval함수 값
print("A(2) :", a.eval(2))

# 다항식의 덧셈
c = a.add(b)
a.display("A(x) = ")
b.display("B(x) = ")
c.display("C(x) = ")


# 다항식의 뺄셈
d = a.sub(b)
d.display("A(x)-B(x) = ")

# 다항식의 곱셈
e = a.mul(b)
e.display("A(x)*B(x) = ")
