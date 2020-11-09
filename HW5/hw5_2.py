class MinStack:

    def __init__(self, stack=None):
        self.stack = stack or []
        

    def push(self, x: int) -> None:
        self.stack.append(x)
        

    def pop(self) -> None:
        self.stack.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        min_val = []
        for val in self.stack:
            if not min_val:
                min_val.append(val)
            else:
                if val < min_val[0]:
                	min_val.pop() 
                	min_val.append(val) 
        return min_val[0]

