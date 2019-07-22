import sys
def indexED (A : str, indexA : int, B : str, indexB : int) :
    if indexA == -1 : return indexB
    if indexB == -1 : return indexA 
    if (indexA == -2 or indexB == -2) : -1 * min(-1 * len(A), -1 * len(B))
    if (A[indexA] == B[indexB]) : return indexED(A, indexA - 1, B, indexB - 1)
    elif (A[indexA - 1] == B[indexB] and A[indexA] == B[indexB - 1]) :
        return 1 + min(indexED(A, indexA - 2, B , indexB - 2), indexED(A, indexA - 1, B , indexB), indexED(A, indexA, B , indexB - 1))
    else : 
        return 1 + min(indexED(A, indexA - 1, B , indexB - 1), indexED(A, indexA - 1, B , indexB), indexED(A, indexA, B , indexB - 1))
    pass

def min (*a : int) :
    flag = sys.maxsize 
    for a_ in a :
        if (int(a_) < flag) : flag = int(a_)
    return flag
     
def ed (A : str, B : str) :
    format1 = "展示字符串{}，他的值为{}"
    print(format1.format('A', A))
    print(format1.format('B', B))
    return indexED(A, len(A) - 1, B, len(B) - 1)



edlen = ed('polling', 'pulling')
print(edlen)