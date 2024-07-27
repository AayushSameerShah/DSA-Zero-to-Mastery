# Given the root of a binary tree, determine if it is a valid binary search tree (BST).

# A valid BST is defined as follows:

# - The left subtree of a node contains only nodes with keys less than the node's key.
# - The right subtree of a node contains only nodes with keys greater than the node's key.
# - Both the left and right subtrees must also be binary search trees.
 

# Example 1:


# Input: root = [2,1,3]
# Output: true
# Example 2:


# Input: root = [5,1,4,null,null,3,6]
# Output: false
# Explanation: The root node's value is 5 but its right child's value is 4.
 

# Constraints:

# The number of nodes in the tree is in the range [1, 104].
# -231 <= Node.val <= 231 - 1

class Queue:
    
    def __init__(self):
        # not optimal, should've used linkedlist, but okay for now
        # for the sake of cleaner code
        self.container = []
        self.size = 0

    
    def enqueue(self, value):
        self.container.append(value)
        self.size += 1
    
    def dequeue(self):
        if self.size > 0:
            self.size -= 1
            return self.container.pop(0)
            
        else:
            raise NotImplementedError("Queue is empty")

class Node:
    '''
    Just so that we will have something to store and carry around
    '''
    def __init__(self, value):
        self.left = None
        self.right = None
        self.value = value


class BinarySearchTree:
    
    def __init__(self) -> None:
        '''
        The `root` pointer will be initialized only. 
        We will insert something later.
        '''
        self.root = None

    def insert(self, value) -> None:
        '''
        Handle the special case of the root, if that's empty, 
        fill it. Potentially wasting a special condition check,
        but I think that's okay for now.
        '''
        newNode = Node(value)
        if self.root is None:
            self.root = newNode
        else: # most of the cases we will come here
            currNode = self.root
            while True: # no recursion needed, this is the linear lookup
                if value < currNode.value: 
                    if currNode.left is None:
                        currNode.left = newNode
                        break
                    currNode = currNode.left
                else:
                    if currNode.right is None:
                        currNode.right = newNode
                        break
                    currNode = currNode.right
    
    def validate_tree(self):
        def go_down_and_check(node, prev, result):
            if node is None: # no child
                return
            
            go_down_and_check(node.left, prev, result)
            if prev[0] and prev[0].value >= node.value:
                result[0] = False
            # keep checking
            prev[0] = node
            go_down_and_check(node.right, prev, result)
        
        node = self.root
        prev = [None]
        result = [True]
        go_down_and_check(node, prev, result)
        return result

BST = BinarySearchTree()

BST.insert(40)
BST.insert(30)
BST.insert(50)
BST.insert(45)
BST.insert(25)
BST.insert(35)
BST.insert(60)
BST.insert(70)
# BST.insert(702)


BST.root.right.left.value = 12


print(BST.validate_tree())