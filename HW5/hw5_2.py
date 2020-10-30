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
        return sorted(self.stack)[0]
