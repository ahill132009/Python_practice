import sys
sys.setrecursionlimit(30000)



def solution(a, b):
    if a == 0:
    	return b 
    return solution(a-1, b+1)

