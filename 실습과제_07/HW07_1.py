# 집합 클래스
class Set :
    def __init__(self):
        self.items = []

    def size(self):
        return len(self.items)
    
    def contains(self, item):
        return item in self.items
    
    def insert(self, elem):
        if elem in self.items: return
        for idx in range(len(self.items)):
            if elem < self.items[idx]:
                self.items.insert(idx, elem)
                return
        self.items.append(elem)

    def delete(self, elem):
        self.items.remove(elem)
    
    def __eq__(self, setB):
        if self.size() != setB.size():
            return False
        for idx in range(len(self.items)):
            if self.items[idx] != setB.items[idx]:
                return False
        return True
    
    # 합집합
    def union(self, setB):
        newSet = Set()
        a = 0
        b = 0
        while a < len(self.items) and b < len(setB.items):
            valueA = self.items[a]
            valueB = setB.items[b]
            if valueA < valueB:
                newSet.items.append(valueA)
                a += 1
            elif valueA > valueB:
                newSet.items.append(valueB)
                b += 1
            else:
                newSet.items.append(valueA)
                a += 1
                b += 1
            
        while a < len(self.items):
            newSet.items.append(self.items[a])
            a += 1
        while b < len(setB.items):
            newSet.items.append(setB.items[b])
            b += 1
        
        return newSet
    
    # 교집합
    def intersect(self, setB):
        SetI = Set()            # 반환할 교집합
        a = 0                   # 집합 self의 원소 인덱스
        b = 0                   # 집합 b의 원소 인덱스

        while a < len(self.items) and b < len(setB.items):
            valueA = self.items[a]          # 집합 self의 현재원소
            valueB = setB.items[b]          # 집합 b의 현재원소
            if valueA < valueB:             # 더 작은 인덱스 번호이동
                a += 1
            elif valueA > valueB:
                b += 1
            elif valueA == valueB:                           # 같은값이면 교집합에 추가
                SetI.items.append(valueA)
                a += 1
                b += 1
        
        return SetI
    
    # 차집합
    def difference(self, setB):
        SetD = Set()            # 차집합 객체 생성
        a = 0                   # 집합 self의 원소 인덱스
        b = 0                   # 집합 b의 원소 인덱스
        
        SetD.items = self.items[:]               # self의 원소 얕은복사
        
        while a < len(SetD.items) and b < len(setB.items):
            valueA = SetD.items[a]          # 차집합의 현재원소
            valueB = setB.items[b]          # 집합 b의 현재원소
            if valueA < valueB:             
                a += 1
            elif valueA > valueB:
                b += 1
            elif valueA == valueB:
                SetD.delete(valueA)
                a += 1
                b += 1
        
        return SetD
            


    def display(self, msg):
        print(msg, self.items)

# ============================================================
setA = Set()
setA.insert('휴대폰')
setA.insert('지갑')
setA.insert('손수건')
setA.display('Set A: ')

setB = Set()
setB.insert('빗')
setB.insert('파이썬 자료구조')
setB.insert('야구공')
setB.insert('지갑')
setB.display('Set B: ')

setB.insert('빗')
setA.delete('손수건')
setA.display('Set A: ')
setB.display('Set B: ')


setA.union(setB).display('A U B: ')
setA.intersect(setB).display('A ^ B: ')
setA.difference(setB).display('A - B: ')



