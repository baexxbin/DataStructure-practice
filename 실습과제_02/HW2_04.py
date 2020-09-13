def printNum(n) :
    if n != 1 :
        printNum(n-1)
    print("%d" %n, end=" ")
printNum(n = int(input("숫자를 입력하세요: ")))
print(sep='\n')

def printRevNum(n) :
    if n == 1 : print('1')
    else:
        print(n, end=" ")
        return printRevNum(n-1)

printRevNum(n = int(input("숫자를 입력하세요: ")))
