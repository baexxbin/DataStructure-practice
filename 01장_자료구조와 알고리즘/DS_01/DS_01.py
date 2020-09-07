
'''
def contains(bag, e):
    return e in bag

def insert(bag, e):
    bag.append(e)

def remove(bag, e):
    bag.remove(e)

def count(bag):
    return len(bag)

def numOf(bag, e):
    count = 0
    for i in range(len(bag)):
        if bag[i] == e :
            count += 1
    return count '''
# ========================
'''
myBag = []
insert(myBag,'아이폰')
insert(myBag,'에어팟')
insert(myBag,'초콜릿')
insert(myBag,'필통')
insert(myBag,'전공책')
insert(myBag,'종이')
print('가방속의 물건:',myBag)

insert(myBag,'과제')
remove(myBag,'초콜릿')
print('가방속의 물건:',myBag)

print('전공책의 개수:',numOf(myBag,'전공책'))'''

# 순환 피보나치

def fib(n):
    if n == 0 : return 0
    elif n == 1 : return 1
    else :
        return fib(n-1) + fib(n-2)

# 반복 피보나치

def fib_iter(n):
    if(n<2): return n

    last = 0
    current = 1
    for i in range(2,n+1):
        tmp = current
        current += last
        last = tmp
    return current

import time

print('Fibonacci반복(7) = ', fib_iter(7))
print('Fibonacci순환(7) = ',fib(7))

for i in range (1,40):
    start = time.time()
    fib(i)
    end = time.time()

    start2 = time.time()
    str(fib_iter(i))
    end2 = time.time()
    print('n=', i, '반복:', end2-start2 , '순환:', end-start)