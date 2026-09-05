
class Queue:
    def __init__(self):
        self.queue = []

    def is_empty(self):
        if len(self.queue) == 0:
            return True
        else:
            return False

    def enqueue(self, item):
        self.queue.append(item)

    def dequeue(self):
        if self.is_empty():
            print("Queue underflow")
        else:
            self.queue.pop(0)
    def peek(self):
        if self.is_empty():
            print("Queue is empty")
        else:
            print(self.queue[0])
queue1 = Queue()
queue1.enqueue("Parsa")
queue1.enqueue("hello")
queue1.enqueue("world")

queue1.dequeue()
queue1.dequeue()
queue1.peek()
queue1.dequeue()
queue1.dequeue()