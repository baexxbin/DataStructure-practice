def bubble_sort(A):
    n = len(A)
    for i in range(n-1, 0, -1):
        bChanged = False
        for j in range(i):
            if (A[j]> A[j+1]):
                A[j], A[j+1] = A[j+1], A[j]
                bChanged = True
            
        if not bChanged: break;
        print(f'step {n-i} = {A}')
    return n-i-1

def ture(A):
    cnt = bubble_sort(A)
    if cnt == 0:
        return True
    else:
        return False

A = [5,3,8,4,9,1,6,2,7]
B = [1,2,3,4,5,6,7,8,9]

print(f'배열 A{A}는 {ture(A)}')
print(f'배열 B{B}는 {ture(B)}')
