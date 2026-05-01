class DNode:
    def __init__(self, data):
        self.data = data
        self.next = self.prev = None

class DLL:
    def __init__(self): self.head = None
    def insert(self, data):
        nn = DNode(data)
        if self.head:
            self.head.prev = nn
            nn.next = self.head
        self.head = nn
    def traverse_back(self):
        t = self.head
        while t.next: t = t.next
        while t:
            print(t.data, end=" <-> ")
            t = t.prev
        print("None")

d = DLL()
d.insert(1); d.insert(2); d.traverse_back()