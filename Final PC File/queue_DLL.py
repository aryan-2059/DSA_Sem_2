class Node:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

class Queue:
    def __init__(self): self.front = self.rear = None
    def enqueue(self, data):
        nn = Node(data)
        if not self.rear: self.front = self.rear = nn
        else:
            self.rear.next = nn
            self.rear = nn
    def dequeue(self):
        if not self.front: return "Empty"
        val = self.front.data
        self.front = self.front.next
        if not self.front: self.rear = None
        return val

q = Queue()
q.enqueue(100);q.enqueue(200); print(q.dequeue())