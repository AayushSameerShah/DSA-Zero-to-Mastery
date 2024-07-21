"""
This is really easy implementation of the BST.
Please look through the code once, you will know.
"""

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
    
    def lookup(self, value):
        '''
        You might get tempted to write the recursion here, but no.
        Just lookup linearly and search.
        '''
        currNode = self.root
        if currNode is None:
            return False
        
        while True:
            if currNode.value < value:
                if currNode.right is not None:
                    currNode = currNode.right
                else:
                    return False
            elif currNode.value > value:
                if currNode.left is not None:
                    currNode = currNode.left
                else:
                    return False
            elif currNode.value == value:
                return currNode

    def delete(self, value):
        '''
        This will have 3 cases. We will need to deal with them.
        Let's first write the pseudo code:
        
        Step - 1: Find the element to delete; if not found return False
        Step - 2: Check the case out of 3
        Step - 3: Make adjustments as per the case.

        ---

        Cases:

        1. The removal node has 2 children.
            - In this case take one step to the right and then keep going for the left
            child until the leaf node is found (which can have None on both sides or have
            single child on the right)
            - Here, replace this "leaf" node for the node to be removed
            - Assign its right child to the immediate parent
        
        2. The removal node is the leaf node and doesn't have any children
            - Make the parent node not to point it.
        
        3. The removal node has single child.
            - Remove this node and assign the its child as a parent of this node
        '''

        # Step - 1: Search


        ## We will track 2 pointers 
        ## The Parent: The immediate parent of the child to be removed (later will be used to point new child)
        ## The child: The actual node to be removed
        is_found = None
        parentNode = None
        currNode = self.root
        
        # finding `that` node to be removed
        while True:
            if currNode.value < value:
                if currNode.right is not None:
                    parentNode = currNode
                    currNode = currNode.right
                else:
                    is_found = False
                    break
            elif currNode.value > value:
                if currNode.left is not None:
                    parentNode = currNode
                    currNode = currNode.left
                else:
                    is_found = False
                    break
            elif currNode.value == value:
                is_found = True
                break

        # return immediately if we are unable to lookup
        if not is_found:
            print(False)
            return False
        
        # Step - 2: Find the case

        # printing the current child and its parent
        print("Current node value:", currNode.value)
        if parentNode is None: # means the deletion node is ROOT itself
            print("Current node's parent is NONE; because it is root node")
        else:
            print("Current node's parent value:", parentNode.value)

        ## Checking if this the first case in which the removal node has children
        if currNode.left is not None and currNode.right is not None: # this is first case
            print("IN THE CASE - 1")
            
            # going first right and immediate last left
            stepParent = None
            stepChild = currNode.right
            print("Step child in first turn", stepChild.value)
            while stepChild.left is not None:
                stepParent = stepChild
                stepChild = stepChild.left
            print("Step child after lefts", stepChild.value)
                
            # okay, now we have reached the farthest left child, does it have any children?
            # (it will have children only on the right side.)
            # if does, then we will need to attach it with its parent
            
            # stepParent will only exist when we have taken left turns
            if stepParent:
                if stepChild.right:
                    stepParent.left = stepChild.right
                else:
                    stepParent.left = None

                # so, finally we have the node which we can replace with
                # assigning the removal node's left and right to the replacable node
                stepChild.left = currNode.left
                stepChild.right = currNode.right
        
            # no left turn? Just update the replace note with the removal left
            else:
                stepChild.left = currNode.left

            # if the removal node is the root itself, then ...
            if parentNode: # the root node edge case check
                if parentNode.value < value:
                    parentNode.right = stepChild
                else:
                    parentNode.left = stepChild
            else:
                self.root = stepChild
                


        elif currNode.left is None and currNode.right is None: # this is the second case
            print("IN THE CASE - 2")
            if parentNode.value < value:
                parentNode.right = None
            else:
                parentNode.left = None
        
        else: # the classic third case
            print("IN THE CASE - 3")
            if parentNode.value < value:
                if currNode.right:
                    parentNode.right = currNode.right
                else:
                    parentNode.right = currNode.left
            else:
                if currNode.right:
                    parentNode.left = currNode.right
                else:
                    parentNode.left = currNode.left



    def traverse(self, node=None):
        '''
        The travarsal of the nodes require little recursion.
        This is cool, just read. 

        In the start, we will pass `None` so that it starts 
        with the root node.
        '''
        if node is None:
            node = self.root
        
        if node is not None:
            print(node.value)  # Visit the node
            if node.left:      # Traverse left subtree
                self.traverse(node.left)
            if node.right:     # Traverse right subtree
                self.traverse(node.right)

        



BST = BinarySearchTree()

BST.insert(40)
BST.insert(30)
BST.insert(50)
BST.insert(45)
BST.insert(25)
BST.insert(35)
BST.insert(60)
BST.insert(70)
BST.traverse()

BST.delete(60)
BST.traverse()



# print(BST.lookup(1702))