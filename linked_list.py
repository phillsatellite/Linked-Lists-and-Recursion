# A Node class to store integer data and a reference to the next node.
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

# A singly linked list that holds Node objects and performs operations using recursion.
class LinkedList:
    def __init__(self):
        self.head = None

    # - Create a new Node with 'data'.
    # - Insert it at the front of the list (head).
    # - Update 'head' to the new node.
    def insert_at_front(self, data):
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    # (Optional)
    # - Create a new Node with 'data'.
    # - Traverse to the end of the list.
    # - Set the last node's 'next' reference to the new node.
    def insert_at_end(self, data):
        new_node = Node(data)
        if not self.head:
            self.head = new_node
            return 
        
        current = self.head
        while current.next:
            current = current.next
        
        current.next = new_node

    # - Use recursion to sum all node data in the list.
    # - Consider a helper function that:
    # 1. Checks if the current node is None, and returns 0 if so.
    # 2. Otherwise, returns node.data + recursive call on node.next.
    # - Return the total sum.
    def recursive_sum(self):
        def helper(node):
            if node is None:
                return 0
            return node.data + helper(node.next)
        return helper(self.head)

    # - Reverse the list in-place using recursion.
    # - Possible approach:
    # 1. Use a helper function that accepts 'prev' and 'current'.
    # 2. Base case: if current is None, return 'prev' (new head).
    # 3. Otherwise, swap pointers and recurse.
    # - Update 'head' to the returned new head.
    def recursive_reverse(self):
        def helper(prev, current):
            if current is None:
                return prev 
            next_node = current.next
            current.next = prev
            return helper(current, next_node)
        
        self.head = helper(None, self.head)

    # - Return True if 'target' is found, otherwise False, using recursion.
    # - Consider a helper function that:
    # 1. Returns False if the current node is None.
    # 2. Returns True if current node's data == target.
    # 3. Otherwise, recurse on the next node.
    def recursive_search(self, target):
        def helper(node):
            if node is None:
                return False
            if node.data == target:
                return True
            return helper(node.next)
        
        return helper(self.head)

    # - Print the contents of the list for debugging.
    # - Traverse from 'head' and collect each node's data.
    # - Format output as 'val -> val -> val -> None' or similar.
    def display(self):
        current = self.head
        values = []

        while current:
            values.append(str(current.data))
            current = current.next
        
        print("->".join(values)+ "-> None")