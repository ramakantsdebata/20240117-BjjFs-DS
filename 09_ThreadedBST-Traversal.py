class ThreadedBinaryTreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None
        self.left_thread = True
        self.right_thread = True

class DoublyThreadedBinaryTree:
    def __init__(self):
        self.root = None
    
    # def createNode(self, val):
    #     node = ThreadedBinaryTreeNode(val)

    def insert(self, val):
        node = ThreadedBinaryTreeNode(val)
        if self.root == None:
            self.root = node
        else:
            temp = self.root

            while True:
                if val < temp.val:
                    if temp.left_thread == True:
                        node.left = temp.left
                        node.right = temp

                        temp.left = node
                        temp.left_thread = False
                        return
                    else:
                        temp = temp.left
                elif val > temp.val:
                    if temp.right_thread == True:
                        node.left = temp
                        node.right = temp.right
                        temp.right = node
                        temp.right_thread = False
                        return
                    else:
                        temp = temp.right
                else:
                    print("Duplicate data; Not adding node.")

    def rightSon(self, curr):
        flag = False
        temp = self.root

        while True:
            while temp.left_thread == False and flag == False:
                temp = temp.left
                if curr == temp:
                    return False
            
            flag = temp.right_thread
            temp = temp.right
            if flag == False and temp == curr:
                return True

            if temp == None:
                break
        
        return False
    

    def threadTraversal(self):
        temp = self.root
        flag = False
        
        if temp == None:
            print("Tree is Empty!")
            return
        

        # Inorder Traversal
        print("Inorder traversal", end='\t')

        while temp != None:
            while temp.left_thread == False and flag == False:
                temp = temp.left

            print(temp.val, end=' ')
            flag = temp.right_thread
            temp = temp.right
        print('')

        # Preorder Travesal
        print("Preorder traversal", end='\t')
        flag = False
        temp = self.root

        while temp != None:
            while temp.left_thread == False and flag == False:
                print(temp.val, end=' ')
                temp = temp.left

            if flag == False:
                print(temp.val, end=' ')
            
            flag = temp.right_thread
            temp = temp.right
        print('')

        # Postorder Traversal
        print("Postorder traversal", end='\t')
        flag = False
        temp = self.root

        while temp != None:
            while temp.left_thread == False and flag == False:
                temp = temp.left

            flag = temp.right_thread
            if flag == False:
                temp = temp.right
            else:
                while True:
                    print(temp.val, end=' ')
                    if self.rightSon(temp):
                        while temp.left_thread == False:
                            temp = temp.left
                        temp = temp.left
                    else:
                        while temp.right_thread == False:
                            temp = temp.right
                        temp = temp.right
                        flag = True
                        break







    #==========================================
    # def insert(self, val):
    #     node = ThreadedBinaryTreeNode(val)
    #     print("\nAdding [%d]\n"%(val))
    #     if self.root is None:
    #         self.root = node
    #         return
    #     curr = self.root
    #     while True:
    #         print("At %d : "%(curr.val), end='')
    #         if val < curr.val:
    #             print("[Left - ", end='')
    #             if curr.left is None:
    #                 print("Add] ", end='')
    #                 node.left = curr.left
    #                 node.right = curr
    #                 node.left_thread = True
    #                 node.right_thread = True
    #                 curr.left = node
    #                 print("[DONE !]\n", end='')
    #                 return
    #             else:
    #                 print("Dive] ", end='')
    #                 curr = curr.left
    #         else:
    #             print("[Right - ", end='')
    #             if curr.right is None:
    #                 print("Add] ", end='')
    #                 node.right = curr.right
    #                 node.left = curr
    #                 node.left_thread = True
    #                 node.right_thread = True
    #                 curr.right = node
    #                 print("[DONE !]\n", end='')
    #                 return
    #             else:
    #                 print("Dive] ", end='')
    #                 curr = curr.right
    
    # def inorder(self):
    #     curr = self.root
    #     while curr is not None:
    #         if curr.left_thread:
    #             curr = curr.left
    #         else:
    #             print(curr.val)
    #             if curr.right_thread:
    #                 curr = curr.right
    #             else:
    #                 curr = curr.right.left
    
    # def preorder(self):
    #     curr = self.root
    #     while curr is not None:
    #         print(curr.val)
    #         if curr.left_thread:
    #             curr = curr.left
    #         else:
    #             if curr.right_thread:
    #                 curr = curr.right
    #             else:
    #                 curr = curr.right.left
    
    # def postorder(self):
    #     curr = self.root
    #     while curr is not None:
    #         if curr.left_thread:
    #             curr = curr.left
    #         else:
    #             if curr.right_thread:
    #                 print(curr.val)
    #                 curr = curr.right
    #             else:
    #                 curr = curr.right.left
    #                 while not curr.left_thread or not curr.right_thread:
    #                     if not curr.left_thread:
    #                         curr = curr.left
    #                     else:
    #                         curr = curr.right
    #                 print(curr.val)

# Example usage
tree = DoublyThreadedBinaryTree()
tree.insert(5)
tree.insert(3)
tree.insert(7)
tree.insert(2)
tree.insert(4)
tree.insert(6)
tree.insert(8)

print("Thread Traversal:")
tree.threadTraversal()

# tree.inorder()

# print("Preorder Traversal:")
# tree.preorder()

# print("Postorder Traversal:")
# tree.postorder()
