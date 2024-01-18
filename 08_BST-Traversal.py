from collections import deque
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None
    
    def insert(self, value):
        new_node = Node(value)
        if not self.root:
            self.root = new_node
        else:
            current = self.root
            while True:
                if value < current.value:
                    if not current.left:
                        current.left = new_node
                        break
                    else:
                        current = current.left
                else:
                    if not current.right:
                        current.right = new_node
                        break
                    else:
                        current = current.right
    
    def print_tree(self, node, level=0):
        if node:
            self.print_tree(node.right, level + 1)
            print(' ' * 4 * level + '->', node.value)
            self.print_tree(node.left, level + 1)

    def pretty_print_tree(self, root, level=0, prefix="Root: ", is_left=None):
        if root is not None:
            print(" " * (level * 5) + prefix, end="")
            print("└── " if is_left else "├── ", end="")
            print(root.value)
            self.pretty_print_tree(root.left, level + 1, "   L: ", True)
            self.pretty_print_tree(root.right, level + 1, "   R: ", False)

    def print_tree_vertically(self, node):
        if not node:
            return

        queue = deque([(node, 0)])  # Initialize the queue with the root node and its level
        current_level = 0
        current_level_nodes = []

        while queue:
            current_node, level = queue.popleft()

            if level > current_level:
                # Print the nodes at the current level
                self.print_nodes(current_level_nodes)
                current_level += 1
                current_level_nodes = []

            current_level_nodes.append(current_node)

            if current_node.left:
                queue.append((current_node.left, level + 1))
            if current_node.right:
                queue.append((current_node.right, level + 1))

        # Print the nodes at the last level
        self.print_nodes(current_level_nodes)

    def print_nodes(self, nodes):
        for node in nodes:
            print(node.value, end=' ')
        print()


# Traversal (Recursive approach)

    # def inorder_traversal(self, node):
    #     if node:
    #         self.inorder_traversal(node.left)
    #         print(node.value, end=' ')
    #         self.inorder_traversal(node.right)
    
    # def preorder_traversal(self, node):
    #     if node:
    #         print(node.value, end=' ')
    #         self.preorder_traversal(node.left)
    #         self.preorder_traversal(node.right)
    
    # def postorder_traversal(self, node):
    #     if node:
    #         self.postorder_traversal(node.left)
    #         self.postorder_traversal(node.right)
    #         print(node.value, end=' ')


# Traversal (Iterative approach)
    def inorder_traversal(self, root):
        # LPR (Left, Parent, Right)
        if not root:
            return []
        stack = []
        result = []
        curr = root
        while curr or stack:
            while curr:
                stack.append(curr)
                curr = curr.left
            curr = stack.pop()
            result.append(curr.value)
            curr = curr.right
        print(result)

    def preorder_traversal(self, root):
        # PLR (Parent, Left, Right)
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            curr = stack.pop()
            result.append(curr.value)
            if curr.right:
                stack.append(curr.right)
            if curr.left:
                stack.append(curr.left)
        print(result)

    def postorder_traversal(self, root):
        # LRP (Left, Right, Parent)
        if not root:
            return []
        stack = [root]
        result = []
        while stack:
            curr = stack.pop()
            result.append(curr.value)
            if curr.left:
                stack.append(curr.left)
            if curr.right:
                stack.append(curr.right)
        print(result[::-1])



# Example usage
bst = BinarySearchTree()
bst.insert(50)
bst.insert(30)
bst.insert(70)
bst.insert(20)
bst.insert(40)
bst.insert(60)
bst.insert(80)

print("Tree:")
bst.print_tree(bst.root)

print("Tree (vertically):")
bst.print_tree_vertically(bst.root)

print("Tree (pretty):")
bst.pretty_print_tree(bst.root)

print("Inorder Traversal:", end=' ')
bst.inorder_traversal(bst.root)

print("\nPreorder Traversal:", end=' ')
bst.preorder_traversal(bst.root)

print("\nPostorder Traversal:", end=' ')
bst.postorder_traversal(bst.root)
