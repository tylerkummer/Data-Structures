"""
Binary search trees are a data structure that enforce an ordering over
the data they store. That ordering in turn makes it a lot more efficient
at searching for a particular piece of data in the tree.

This part of the project comprises two days:
1. Implement the methods `insert`, `contains`, `get_max`, and `for_each`
   on the BSTNode class.
2. Implement the `in_order_print`, `bft_print`, and `dft_print` methods
   on the BSTNode class.
"""
from queue import Queue
from stack import Stack


class BSTNode:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # Case 1: value is less than self.value
        if value < self.value:
            # If there is no left child, insert value here
            if self.left is None:
                self.left = BSTNode(value)
            else:
                # Repeat the process on left subtree
                self.left.insert(value)

        # Case 2: value is greater than or equal self.value
        elif value >= self.value:
            # If there is no right child, insert value here
            if self.right is None:
                self.right = BSTNode(value)
            else:
                # Repeat the process on right subtree
                self.right.insert(value)

    # Return True if the tree contains the value
    # False if it does not
    def contains(self, target):
        # Case 1: self.value is equal to the target
        if self.value == target:
            return True

        # Case 2: target is less than self.value
        if target < self.value:
            # if self.left is None, it isn't in the tree
            if self.left is None:
                return False
            else:
                return self.left.contains(target)

        # Case 3: otherwise
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

    # Return the maximum value found in the tree
    def get_max(self):
        # forget about the left subtree
        # iterate through the nodes using a loop construct

        # Check if node has value if not break out
        if self.value is None:
            return

        # If right side of node is empty then its the max value and return it
        if self.right is None:
            return self.value
        # If right side of node is populated then use recursion to re run the function to the next right value
        # repeat process until the right side of node is empty
        else:
            return self.right.get_max()

    # Call the function `fn` on the value of each node
    def for_each(self, fn):
        # Check if node has value if not break out
        if self.value is None:
            return

        # Apply function to the node
        fn(self.value)
        # Apply function the the right of the node if it exists
        if self.right is not None:
            self.right.for_each(fn)
        # Apply function to the left of the node if it exists
        if self.left is not None:
            self.left.for_each(fn)

    # Part 2 -----------------------

    # Print all the values in order from low to high
    # Hint:  Use a recursive, depth first traversal
    def in_order_print(self, node):
        # if the current node is None
        # we know we've reached the end of a recursion
        # (base case) we want to return
        if self is None:
            return
        # check if we can "move left"
        if self.left is not None:
            self.left.in_order_print(node.left)
        # visit the node by printing its value
        print(self.value)
        # check if we can "move right"
        if self.right is not None:
            self.right.in_order_print(node.right)

    # Print the value of every node, starting with the given node,
    # in an iterative breadth first traversal
    def bft_print(self, node):
        # You should import the queue class from earlier in the
        # week and use that class to implement this method
        # Use a queue to form a "line"
        # for the nodes to "get in"
        queue = Queue()
        # start by placing the root in the queue
        queue.enqueue(node)
        # need a while loop to iterate
        # what are we checking in the while statement?
        # while length of queue is greater than 0
        while(queue.size > 0):
            # dequeue item from front of queue
            queue_deq = queue.dequeue()
            # print that item
            print(queue_deq.value)
            # place current item's left node in queue if not None
            if queue_deq.left is not None:
                queue.enqueue(queue_deq.left)
            # place current item's right node in queue if not None
            if queue_deq.right is not None:
                queue.enqueue(queue_deq.right)

    # Print the value of every node, starting with the given node,
    # in an iterative depth first traversal
    def dft_print(self, node):
        # initialize an empty stack
        stack = Stack()
        # push the root node onto the stack
        stack.push(node)
        # need a while loop to manager our iteration
        # if stack is not empty enter the while loop
        while(stack.size > 0):
            # pop top item off the stack
            stack_pop = stack.pop()
            # print that item's value
            print(stack_pop.value)
            # if there is a right subtree
            if stack_pop.right is not None:
                # push right item onto the stack
                stack.push(stack_pop.right)
            # if there is a left subtree
            if stack_pop.left is not None:
                # push left item onto the stack
                stack.push(stack_pop.left)

    # Stretch Goals -------------------------
    # Note: Research may be required

    # Print Pre-order recursive DFT
    # def pre_order_dft(self, node):
    #     pass

    # Print Post-order recursive DFT
    # def post_order_dft(self, node):
    #     pass
