# 엔트리__맵의 요소(키:값)
class Entry:
    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __str__(self):
        return str("%s:%s"%(self.key, self.value))


# 선형조사법 맵
class LinearProbMap:
    # 생성자__테이블 설정
    def __init__(self, M):
        self.table = [None]*M               
        self.M = M

    # 해시함수__[문자열 테이블크기 처리]
    def hashFn(self, key):
        sum = 0
        for c in key:
            sum = sum + ord(c)
        return sum % self.M
    
    # 삽입연산
    def insert(self, key, value):
        idx = self.hashFn(key)          # idx의 키값 찾기
        while self.table[idx] != None:  # None이 아닐동안 반복(값을 넣는 조건)
            idx = (idx+1) % self.M      # idx이동
        self.table[idx] = Entry(key, value)     # 값 삽입


    
    # 탐색연산
    def search(self, key):
        idx = self.hashFn(key)                  # idx == 키값
        origin_idx = idx                        # 예외처리를 위한 원래 idx값 저장
        while self.table[idx] != None:          # None이면 탐색끝
            if self.table[idx] != False:        # False값도 아닐때
                if self.table[idx].key == key:  # 탐색할 얘 찾으면 
                    return self.table[idx]      # 반환
                else:                           # 탐색할 얘 못찾으면
                    idx = (idx+1) % self.M      # idx 이동
            else:                               # False값일때 처리
                idx = (idx+1) % self.M          # idx 이동
            if idx == origin_idx:               # 예외처리(테이블이 꽉차있을때)
                return None
        return None
                

    # 삭제연산
    def delete(self, key):
        idx = self.hashFn(key)      
        while self.table[idx] != None and self.table[idx] != False:
            if (self.table[idx].key == key):
                self.table[idx] = False
            else:
                idx = (idx+1) % self.M
                

    
    # 출력
    def display(self, msg):
        print(msg)
        for idx in range(len(self.table)):
            slot = self.table[idx]
            if slot is not None:
                print("[%2d] -> " %idx, self.table[idx])

# =====================================================
map = LinearProbMap(13)
map.insert('data', '자료')
map.insert('structure', '구조')
map.insert('sequential search', '선형탐색')
map.insert('game', '게임')
map.insert('binary search', '이진 탐색')
map.display("나의 단어장: ")

print(" 탐색:game —> ", map.search('game'))
print(" 탐색:over —> ", map.search('over'))
print(" 탐색:data —> ", map.search('data'))
map.delete('game')
map.display("나의 단어장: ")
print(" 탐색:game —> ", map.search('game'))