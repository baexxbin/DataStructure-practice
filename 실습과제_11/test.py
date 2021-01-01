import math

class Figure:
    def __init__(self, points):
        self.p = points
    def getName(self):
        print(f'도형의 이름')
    
    def getArea(self):
        print(f'도형의 넓이')
    

class Line(Figure):
    def __init__(self):     # points 이차원 배열[[]]
        super().__init__(points)
    
    def getName(self):
        print('직선 입니다.')
    
    def getArea(self):
        leng = math.sqrt(pow(self.p[1][0]-self.p[0][0],2) + pow(self.p[1][1]-self.p[0][1],2))
        print(f'길이는 {leng} 입니다.')

        
class Rectangle(Figure):
    def __init__(self):      # points 일차원 배열 []
        super().__init__(points)
        
    def getName(self):
        print('사각형 입니다.')
        
    def getArea(self):
        area = self.p[0][0]*self.p[0][1]
        print(f'넓이는 {area} 입니다.')
        
    
class Triangle(Figure):
    def __init(self):       # points 이차원 배열 [[],[],[]]
        super().__init__(points)
        
    def getName(self):
        print('삼각형 입니다.')
        
    def getArea(self):
        area = 0.5 * abs( (self.p[0][0] * self.p[1][1] + self.p[1][0] * self.p[2][1] + self.p[2][0] * self.p[0][1]) - (self.p[1][0] * self.p[0][1] + self.p[2][0] * self.p[1][1] + self.p[0][0] * self.p[2][1]) )
        print(f'넓이는 {area} 입니다.')

        
points = list(map(eval,input('값을 입력하세요: ').split()))

if len(points)==1:
    r = Rectangle()
    r.getName()
    r.getArea()

elif len(points)==2:
    l = Line()
    l.getName()
    l.getArea()

elif len(points)==3:
    t = Triangle(points)
    t.getName()
    t.getArea()