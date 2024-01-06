class Stack:
    def add(self, value):
        self.stack.append(value)
        return value

    def pop(self):
        if not self.stack:
            return None
        value = self.stack[-1]
        self.stack = self.stack[:-1]
        return value

    def peek(self):
        if not self.stack:
            return None
        return self.stack[-1]

    def __init__(self):
        self.stack = []
