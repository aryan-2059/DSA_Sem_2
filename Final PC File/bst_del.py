class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
def insert(root, key):
    if root is None:
        return Node(key)
    if key < root.val:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root
def inorder(root):
    if root:
        inorder(root.left)
        print(root.val, end=" ")
        inorder(root.right)
def min_value_node(node):
    curr = node
    while curr.left:
        curr = curr.left
    return curr
def delete_node(root, key):
    if root is None:
        return root

    if key < root.val:
        root.left = delete_node(root.left, key)

    elif key > root.val:
        root.right = delete_node(root.right, key)

    else:
        # Case 1: Leaf node
        if root.left is None and root.right is None:
            return None

        # Case 2: One child
        elif root.left is None:
            return root.right
        elif root.right is None:
            return root.left

        # Case 3: Two children
        temp = min_value_node(root.right)  # inorder successor
        root.val = temp.val
        root.right = delete_node(root.right, temp.val)

    return root
# Build BST
root = None
values = [50, 30, 70, 20, 40, 60, 80]

for v in values:
    root = insert(root, v)

print("Initial Inorder:")
inorder(root)
print("\n")

# Deletions
delete_keys = [20, 30, 50]

for key in delete_keys:
    print(f"Deleting {key}...")
    root = delete_node(root, key)
    print("Inorder after deletion:", end=" ")
    inorder(root)
    print("\n")