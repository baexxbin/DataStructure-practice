# stack 클래스 생성
class Stack:
    def __init__(self):    # 생성자
        self.top = list()
    
    def isEmpty(self): return len(self.top) == 0    # 공백상태이면 항목의 갯수 0
    def size(self): return len(self.top)    # 리스트의 항목개수
    def clear(self): return self.top == []  # 스택을 공백상태로 만듬

    # 삽입연산
    def push(self, item):
        self.top.append(item)
    
    # 삭제연산
    def pop(self):
        if not self.isEmpty():
            return self.top.pop(-1)
    
    # 마지막 항목 반환
    def peek(self):
        if not self.isEmpty():
            return self.top[-1]


# 괄호검사 구현
def isValidSource(lines):
    stack = Stack()
    lcnt = 0
    ccnt = 0
    for line in lines:
        lcnt += 1
        for ch in line:
            ccnt += 1
            if ch in ('{','[','('):
                stack.push(ch)
            elif ch in ('}', ']', ')'):
                if stack.isEmpty():
                    eCode = 2
                    return eCode, lcnt, ccnt
                else :
                    left = stack.pop()
                    if  (ch == "}" and left != "{") or \
                        (ch == "]" and left != "[")or \
                        (ch == ")" and left != "(") :
                        eCode = 3
                        return eCode, lcnt, ccnt
    if stack.isEmpty == False:
        eCode = 1
        return eCode, lcnt, ccnt
    else :
        eCode = 0
        return eCode, lcnt, ccnt

# 실행하기
# filename = "ArrayStack.h"
filename = "CheckBracketMain.cpp"
# filename = "test.py"
# print('스택의 응용1: 괄호검사 %s\n'%filename)
# filename = input("검사할 파일 이름: ")

infile = open(filename, "r", encoding="UTF-8")
lines = infile.readlines();
infile.close()

eCode, lcnt, ccnt = isValidSource(lines)
print(filename, "—>", eCode)
print(" 라인수 = ", lcnt)
print(" 문자수 = ", ccnt)