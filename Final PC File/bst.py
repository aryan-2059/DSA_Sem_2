class BSTNode:
    def __init__(self, key):
        self.left = self.right = None
        self.val = key

def insert(root, key):
    if root is None: return BSTNode(key)
    if key < root.val: root.left = insert(root.left, key)
    else: root.right = insert(root.right, key)
    return root

def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)

r = insert(None, 50); insert(r, 30); insert(r, 70); inorder(r)