class MinStack:

    def __init__(self):
        self.stack = []
        # [1, 1]
        # [1, 2]
        self.min_vals = []
        

    def push(self, val: int) -> None:
        self.stack.append(val)
        if self.min_vals:
            self.min_vals.append(min(self.min_vals[-1], val))
        else:
            self.min_vals.append(val)
        

    def pop(self) -> None:
        self.stack.pop()
        self.min_vals.pop()
        

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.min_vals[-1]
