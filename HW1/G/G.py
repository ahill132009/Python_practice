def solution(a, b):
    return sorted(a + [x for x in b if x in (set(b) - set(a))])
