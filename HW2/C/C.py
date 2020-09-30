def solution(A):

    result = []
    t = 0
    b = len(A)-1
    l = 0
    r = len(A[0])-1
    d = 0
    k = 0
    while(t <= b and l <= r):
        if d == 0:
            for i in range(l,r+1):
                result.append(A[t][i])
            t += 1
            d = 1
        elif d == 1:
            for i in range(t,b+1):
                result.append(A[i][r])
            r -= 1
            d = 2
        elif d == 2:
            for i in range(r,l-1,-1):
                result.append(A[b][i])
            b -= 1
            d = 3
        elif d == 3:
            for i in range(b,t-1,-1):
                result.append(A[i][l])
            l += 1
            d = 0
    return result