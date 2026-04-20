from collections import deque

class BSTNode:
    def __init__(self, key):
        self.key   = key
        self.left  = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    def insert(self, key):
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        if node is None:
            return BSTNode(key)
        if key < node.key:
            node.left  = self._insert(node.left,  key)
        elif key > node.key:
            node.right = self._insert(node.right, key)
        # Duplicate keys are ignored
        return node

    def search(self, key):
        return self._search(self.root, key)

    def _search(self, node, key):
        if node is None:
            return False
        if key == node.key:
            return True
        elif key < node.key:
            return self._search(node.left,  key)
        else:
            return self._search(node.right, key)

    def delete(self, key):
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        if node is None:
            print(f"  Key {key} not found.")
            return node

        if key < node.key:
            node.left  = self._delete(node.left,  key)
        elif key > node.key:
            node.right = self._delete(node.right, key)
        else:
            # CASE 1: Leaf node (no children)
            if node.left is None and node.right is None:
                return None

            # CASE 2: One child
            elif node.left is None:
                return node.right
            elif node.right is None:
                return node.left

            # CASE 3: Two children
            # Find inorder successor (smallest in right subtree)
            else:
                successor = self._find_min(node.right)
                node.key  = successor.key                     # Copy successor's key
                node.right = self._delete(node.right, successor.key)  # Delete successor

        return node

    def _find_min(self, node):
        """Returns the node with minimum key in a subtree."""
        while node.left is not None:
            node = node.left
        return node

    # ---- INORDER TRAVERSAL ----
    def inorder_traversal(self):
        result = []
        self._inorder(self.root, result)
        return result

    def _inorder(self, node, result):
        if node is not None:
            self._inorder(node.left, result)
            result.append(node.key)
            self._inorder(node.right, result)



class Graph:
    def __init__(self, directed=True):
        self.adj_list = {}   
        self.directed = directed

    def add_node(self, node):
        if node not in self.adj_list:
            self.adj_list[node] = []

    def add_edge(self, src, dst, weight=1):
        self.add_node(src)
        self.add_node(dst)
        self.adj_list[src].append((dst, weight))
        if not self.directed:
            self.adj_list[dst].append((src, weight))

    def print_adjacency_list(self):
        print("  Adjacency List:")
        for node in self.adj_list:
            edges = ", ".join(f"{nb}({w})" for nb, w in self.adj_list[node])
            print(f"    {node} -> [{edges}]")

    def bfs(self, start):
        visited = set()
        queue   = deque([start])
        order   = []
        visited.add(start)

        while queue:
            node = queue.popleft()
            order.append(node)
            for neighbor, _ in self.adj_list.get(node, []):
                if neighbor not in visited:
                    visited.add(neighbor)
                    queue.append(neighbor)

        return order

    def dfs(self, start):
        visited = set()
        order   = []
        self._dfs_helper(start, visited, order)
        return order

    def _dfs_helper(self, node, visited, order):
        visited.add(node)
        order.append(node)
        for neighbor, _ in self.adj_list.get(node, []):
            if neighbor not in visited:
                self._dfs_helper(neighbor, visited, order)


class HashTable:
    def __init__(self, table_size=5):
        self.table_size = table_size
        self.table = [[] for _ in range(table_size)]
        self.count = 0

    def _hash(self, key):
        return key % self.table_size

    def insert(self, key, value):
        index  = self._hash(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                pair[1] = value
                return
        bucket.append([key, value])
        self.count += 1

    def get(self, key):
        index  = self._hash(key)
        bucket = self.table[index]
        for pair in bucket:
            if pair[0] == key:
                return pair[1]
        return None  

    def delete(self, key):
        index  = self._hash(key)
        bucket = self.table[index]
        for i, pair in enumerate(bucket):
            if pair[0] == key:
                bucket.pop(i)
                self.count -= 1
                return True
        print(f"  Key {key} not found.")
        return False

    def print_table(self):
        print(f"  Hash Table (size={self.table_size}):")
        for i, bucket in enumerate(self.table):
            content = " -> ".join(f"({k},{v})" for k, v in bucket) if bucket else "EMPTY"
            print(f"    Bucket[{i}]: {content}")


if __name__ == "__main__":

    # BST Test Cases    
    print("=" * 60)
    print("TASK 1: BINARY SEARCH TREE")
    print("=" * 60)

    bst = BST()

    print("\n[Test 1.1] Insert: [50, 30, 70, 20, 40, 60, 80]")
    for val in [50, 30, 70, 20, 40, 60, 80]:
        bst.insert(val)
    print(f"  Inorder: {bst.inorder_traversal()}")

    print("\n[Test 1.2] Search")
    print(f"  Search 20: {bst.search(20)}")  
    print(f"  Search 90: {bst.search(90)}")   

    print("\n[Test 1.3] Delete LEAF node: 20")
    bst.delete(20)
    print(f"  Inorder after deleting 20: {bst.inorder_traversal()}")

    print("\n[Test 1.4] Delete node with ONE CHILD")
    print("  Inserting 65 (child of 70, left side)...")
    bst.insert(65)
    print(f"  Inorder after inserting 65: {bst.inorder_traversal()}")
    print("  Deleting 60 (has one child: 65)...")
    bst.delete(60)
    print(f"  Inorder after deleting 60: {bst.inorder_traversal()}")

    print("\n[Test 1.5] Delete node with TWO CHILDREN: 30")
    bst.delete(30)
    print(f"  Inorder after deleting 30: {bst.inorder_traversal()}")

    print("\n[Test 1.6] Delete ROOT (50) — two children")
    bst.delete(50)
    print(f"  Inorder after deleting 50: {bst.inorder_traversal()}")

    print("\n[Test 1.7] Delete non-existent key: 999")
    bst.delete(999)

    # Graph Test Cases
    print("\n" + "=" * 60)
    print("TASK 2: GRAPH — BFS & DFS")
    print("=" * 60)

    g = Graph(directed=True)

    edges = [
        ('A','B',2), ('A','C',4),
        ('B','D',7), ('B','E',3),
        ('C','E',1), ('C','F',8),
        ('D','F',5),
        ('E','D',2), ('E','F',6),
    ]
    for src, dst, w in edges:
        g.add_edge(src, dst, w)

    print()
    g.print_adjacency_list()

    print(f"\n  BFS from A: {g.bfs('A')}")
    print(f"  DFS from A: {g.dfs('A')}")

    # Hash Table Test Cases
    print("\n" + "=" * 60)
    print("TASK 3: HASH TABLE — SEPARATE CHAINING")
    print("=" * 60)

    ht = HashTable(table_size=5)

    print("\n[Test 3.1] Insert keys: 10, 15, 20, 7, 12")
    print("  Hash function: key % 5")
    print("  Expected collisions: 10%5=0, 15%5=0, 20%5=0 all → Bucket[0]")
    print("                       7%5=2, 12%5=2 both → Bucket[2]")
    for key, val in [(10,'ten'), (15,'fifteen'), (20,'twenty'), (7,'seven'), (12,'twelve')]:
        ht.insert(key, val)

    print()
    ht.print_table()

    print("\n[Test 3.2] Get keys: 15, 7, 20")
    print(f"  get(15) = {ht.get(15)}")
    print(f"  get(7)  = {ht.get(7)}")
    print(f"  get(20) = {ht.get(20)}")
    print(f"  get(99) = {ht.get(99)}  (not found → None)")

    print("\n[Test 3.3] Delete key 15 from Bucket[0] (collided bucket)")
    ht.delete(15)
    print("  After deleting 15:")
    ht.print_table()

    print("\n[Test 3.4] Delete key 99 (does not exist)")
    ht.delete(99)