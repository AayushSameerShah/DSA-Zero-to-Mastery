"""
We will start with the BST. It will only have 2 children. 
We will see what happens next.
"""
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
    

    ## NOTE:
    # The DELETE & LOOKUP functions are removed here. Because we don't need that and 
    # waste space.
    ## 

    def preorder(self, curr_node):
        print(curr_node.value)

        left = curr_node.left
        right = curr_node.right

        if left:
            self.preorder(left)
        if right:
            self.preorder(right)

    def inorder(self, curr_node):
        left = curr_node.left
        right = curr_node.right

        if left:
            self.inorder(left)
        
        print(curr_node.value)
        
        if right:
            self.inorder(right)


    def postorder(self, curr_node):
        left = curr_node.left
        right = curr_node.right

        if left:
            self.postorder(left)
        
        if right:
            self.postorder(right)

        print(curr_node.value)

BST = BinarySearchTree()

BST.insert(40)
BST.insert(30)
BST.insert(50)
BST.insert(45)
BST.insert(25)
BST.insert(35)
BST.insert(60)
BST.insert(70)

print("--- IN ORDER ---")
BST.inorder(BST.root)
print("--- PRE ORDER ---")
BST.preorder(BST.root)
print("--- POST ORDER ---")
BST.postorder(BST.root)