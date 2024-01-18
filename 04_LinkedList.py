class Node:
    def __init__(self, data=None, next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None
    
    # Insertion at the end of the list
    def insert(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
        else:
            current_node = self.head
            while current_node.next is not None:
                current_node = current_node.next
            current_node.next = new_node
    
    # Deletion by value
    def delete(self, value):
        if self.head is None:
            return
        if self.head.data == value:
            self.head = self.head.next
            return
        current_node = self.head
        while current_node.next is not None:
            if current_node.next.data == value:
                current_node.next = current_node.next.next
                return
            current_node = current_node.next
    
    # Reverse the linked list (Iterative)
    def reverse_iterative(self):
        previous_node = None
        current_node = self.head
        while current_node is not None:
            next_node = current_node.next
            current_node.next = previous_node
            previous_node = current_node
            current_node = next_node
        self.head = previous_node
    
    # Reverse the linked list (Recursive)
    def reverse_recursive(self):
        def reverse_util(node):
            if node.next is None:
                return node
            rest = node.next
            rest = reverse_util(rest)
            node.next.next = node
            node.next = None
            return rest
        
        self.head = reverse_util(self.head)

    # Reverse the linked list (Tail Recursive)
    def reverse_tail_recursive(self):
        def reverse_util(current, prev):
            if current.next is None:
                self.head = current
                current.next = prev
                return
            # Save the next node for recursive call
            next_node = current.next
            # And then make the current node point to the previous node
            current.next = prev
            reverse_util(next_node, current)

        reverse_util(self.head, None)

    # Reverse the linked list (using Stack)
    def reverse_stack(self):
        stack = []
        current_node = self.head
        while current_node is not None:
            stack.append(current_node)
            current_node = current_node.next
        self.head = stack.pop()
        current_node = self.head
        while len(stack) > 0:
            current_node.next = stack.pop()
            current_node = current_node.next
        current_node.next = None


    # Print the linked list
    def display(self):
        current_node = self.head
        while current_node is not None:
            print(current_node.data, end=" ")
            current_node = current_node.next
        print()

# Create a linked list and insert some values
ll = LinkedList()
ll.insert(1)
ll.insert(2)
ll.insert(3)
ll.insert(4)
ll.insert(5)

# Print the original linked list
print("Original linked list:")
ll.display()

# Delete a value and print the linked list again
ll.delete(3)
print("Linked list after deleting 3:")
ll.display()

# Reverse the linked list and print it again
ll.reverse_iterative()
print("Linked list after iterative reversal:")
ll.display()

# Reverse the linked list again and print it again
ll.reverse_recursive()
print("Linked list after recursive reversal:")
ll.display()

# Reverse the linked list again and print it again
ll.reverse_tail_recursive()
print("Linked list after tail recursive reversal:")
ll.display()

# Reverse the linked list again and print it again
ll.reverse_stack()
print("Linked list after stack-based reversal:")
ll.display()