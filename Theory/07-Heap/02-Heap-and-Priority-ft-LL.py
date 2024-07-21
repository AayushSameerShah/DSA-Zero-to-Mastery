'''
Heads up.

The Heap implemetation using "nodes" is very slow.
It requires many pointers and travarsal.

The industry implementation uses the "arrays" as they
have the predictable structure and easier indexing.

Here, just to show-off my skills, I will be implementig 
the heaps with nodes.

This is the extreme version and is not official. I have 
made each node to point to parent, left and right siblings
and also 2 children.

This is going to get crazy! Let's do it.
'''

class Node:
    def __init__(self, value) -> None:
        self.value = value
        self.parent = None
        self.left_sib = None
        self.right_sib = None
        self.left_child = None
        self.right_child = None

        # to fast seek the "next current" pointer
        self.edge_node = False

    def __str__(self) -> str:
        value = self.value
        parent = None if self.parent is None else self.parent.value
        left_sib = None if self.left_sib is None else self.left_sib.value
        right_sib = None if self.right_sib is None else self.right_sib.value
        left_child = None if self.left_child is None else self.left_child.value
        right_child = None if self.right_child is None else self.right_child.value
        
        printer = \
f"""
Edge: {self.edge_node}
Value: {value}
Parent: {parent}
Left-sib: {left_sib} | Right-sib: {right_sib}
Left-child: {left_child} | Right-child: {right_child}
"""
        return printer


class Heap:
    def __init__(self) -> None:
        self.root = None
        self.current_node = None
        self.next_current = None

    def insert_batch(self, values):
        for value in values:
            self.insert(value)
    
    def insert(self, value):
        new_node = Node(value)
        if self.root is None:
            new_node.edge_node = True
            self.root = new_node
            self.current_node = self.root
            return self
        
        # checking which child is empty.
        if self.current_node.left_child is None:
            if self.current_node.edge_node == True:
                new_node.edge_node = True
                self.next_current = new_node
            
            self.current_node.left_child = new_node
            new_node.parent = self.current_node

            # attaching the parent's sibling's right child (cousin)
            if new_node.parent.left_sib:
                cousin = new_node.parent.left_sib.right_child
                cousin.right_sib = new_node
                new_node.left_sib = cousin
        
        elif self.current_node.right_child is None:
            self.current_node.right_child = new_node
            new_node.parent = self.current_node

            # getting to know the sibling (since this is right, there will always be the left)
            new_node.left_sib = new_node.parent.left_child
            new_node.parent.left_child.right_sib = new_node

            # since we are on the right child, we will need to move the current node.
            self._move_current_node()

        else: # both are full
            raise NotImplementedError("There is the problem.")
        
        # heapify from this node
        self._heapify(new_node)

    def _move_current_node(self):
        if self.current_node.right_sib is not None:
            self.current_node = self.current_node.right_sib
        else:
            self.current_node = self.next_current

    def _heapify(self, current_node):
        while current_node is not None and current_node.parent is not None:
            if current_node.value <= current_node.parent.value:
                break
            else:
                current_node.value, current_node.parent.value = current_node.parent.value, current_node.value
                current_node = current_node.parent

    def traverse(self):
        curr_node = self.root
        next_node = self.root.left_child
    
        while curr_node:
            print(curr_node.value)
            
            if curr_node.right_sib is None:
                curr_node = next_node
                if curr_node:
                    next_node = curr_node.left_child
                else:
                    next_node = None
            else:
                curr_node = curr_node.right_sib


heap = Heap()

heap.insert_batch([3, 2, 1, 44, 23, 2, 22, 44, 55, 33, 23])
heap.traverse()



