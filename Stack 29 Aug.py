
class Stack:
    def __init__(self):
       self.stack = []

    def is_empty(self):
        if len(self.stack) == 0:
            return True
        else:
            return False
        
    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if self.is_empty():
            print("Stack underflow")
        else:
            self.stack.pop()

    def peek(self): 
        if self.is_empty():
            print("Stack is empty")
        else:

            print(self.stack[-1])

stack1 = Stack()
stack1.push("Parsa")
stack1.push("hello")
stack1.push("world")

stack1.peek()
stack1.pop()
stack1.peek()
stack1.pop()
stack1.pop()
stack1.peek()
stack1.pop()