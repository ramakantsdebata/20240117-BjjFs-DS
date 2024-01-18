class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.height = 1

class AVLTree:
    def insert(self, root, val):
        if not root:
            return Node(val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
        else:
            root.right = self.insert(root.right, val)

        root.height = 1 + max(self.get_height(root.left), self.get_height(root.right))

        balance = self.get_balance(root)

        if balance > 1 and val < root.left.val:
            return self.right_rotate(root)

        if balance < -1 and val > root.right.val:
            return self.left_rotate(root)

        if balance > 1 and val > root.left.val:
            root.left = self.left_rotate(root.left)
            return self.right_rotate(root)

        if balance < -1 and val < root.right.val:
            root.right = self.right_rotate(root.right)
            return self.left_rotate(root)

        return root

    def left_rotate(self, z):
        y = z.right
        T2 = y.left

        y.left = z
        z.right = T2

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def right_rotate(self, z):
        y = z.left
        T3 = y.right

        y.right = z
        z.left = T3

        z.height = 1 + max(self.get_height(z.left), self.get_height(z.right))
        y.height = 1 + max(self.get_height(y.left), self.get_height(y.right))

        return y

    def get_height(self, root):
        if not root:
            return 0
        return root.height

    def get_balance(self, root):
        if not root:
            return 0
        return self.get_height(root.left) - self.get_height(root.right)

    def inorder_traversal(self, root):
        if not root:
            return
        self.inorder_traversal(root.left)
        print(root.val, end=' ')
        self.inorder_traversal(root.right)

    def preorder_traversal(self, root):
        if not root:
            return
        print(root.val, end=' ')
        self.preorder_traversal(root.left)
        self.preorder_traversal(root.right)

    def postorder_traversal(self, root):
        if not root:
            return
        self.postorder_traversal(root.left)
        self.postorder_traversal(root.right)
        print(root.val, end=' ')


# create an AVL tree object
avl_tree = AVLTree()

# insert nodes into the tree
root = None
root = avl_tree.insert(root, 10)
root = avl_tree.insert(root, 20)
root = avl_tree.insert(root, 30)
root = avl_tree.insert(root, 40)
root = avl_tree.insert(root, 50)
root = avl_tree.insert(root, 25)

# perform inorder traversal
print("Inorder Traversal:", end='\t')
avl_tree.inorder_traversal(root)
print()

# perform preorder traversal
print("Preorder Traversal:", end='\t')
avl_tree.preorder_traversal(root)
print()

# perform postorder traversal
print("Postorder Traversal:", end='\t')
avl_tree.postorder_traversal(root)
print()
