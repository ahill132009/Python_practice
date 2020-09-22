def solution(n):
    return'   _~_   ' * n  + '\n' + '  (o o)  ' * n + '\n' + ' /  V  \\ ' * n + '\n' + \
    '/(  _  )\\' * n + '\n' + '  ^^ ^^  ' * n if n else ''
    
print(solution(5))