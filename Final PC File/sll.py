class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class SLL:
    def __init__(self): self.head = None
    
    def insert(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("None")

s = SLL()
s.insert(10); s.insert(20); s.display()