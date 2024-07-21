'''
The ultimate version of heap with array.

> The given version doesn't implement the removal. But that's simple as hell.

Supported features:
- Insert
- Heapify
- Traverse
'''
import numpy as np # will use it

class Heap:
    def __init__(self, value) -> None:
        self.heap = np.full(shape=3, 
                            fill_value=np.nan)
        self.heap[0] = value
        self.pointer = 0
        self.left = True
        self.last_node = 0

    def insert(self, value) -> None:
        # print(self.heap)
        # print("Value: {} and Pointer: {}".format(value, self.pointer))
        self._check_and_expand()
        if self.left == True: # need to assign to the left
            point = self.pointer * 2 + 1
            self.heap[point] = value
            self.left = False
        else:
            point = self.pointer * 2 + 2
            self.heap[point] = value
            self.left = True
            self.pointer += 1 # since the right one is done now.
        self.last_node +=1
        self._heapify()


    def _check_and_expand(self) -> None:
        '''
        This will check if the current size of the array
        is sufficient. Else, it will expand the array.
        '''

        if len(self.heap) <= (self.pointer + 1) * 2:
            new_heap = np.full(len(self.heap) * 2, np.nan)
            new_heap[:len(self.heap)] = self.heap
            self.heap = new_heap
            print("NEW HEAP OF SIZE `{}`".format(len(self.heap)))

    def _heapify(self):
        visitor = self.last_node
        print(f"INSIDE HEAPIFY VISITOR: {visitor}")
        
        def is_child_greater_than_parent(visitor):
            if visitor % 2 == 0 : # right child
                parent = (visitor - 2) // 2
                print("IN RIGHT", parent)
                if visitor == 0:
                    return None, False
                else:
                    return parent, self.heap[visitor] > self.heap[parent] 
            else: # left child
                parent = (visitor - 1) // 2
                print("IN LEFT", parent)
                if visitor == 0:
                    return None, False
                else:
                    return parent, self.heap[visitor] > self.heap[parent] 

        parent, is_child_greater = is_child_greater_than_parent(visitor)
        while is_child_greater:
            self.heap[parent], self.heap[visitor] = self.heap[visitor], self.heap[parent]
            visitor = parent
            parent, is_child_greater = is_child_greater_than_parent(visitor)


    

    def traverse(self):
        i = 0
        while True:
            left = i * 2 + 1
            right = i * 2 + 2
            if left >= len(self.heap):
                left_value = "OT"
            else:
                left_value = self.heap[left]
            
            if right >= len(self.heap):
                right_value = "OT"
            else:
                right_value = self.heap[right]
            
            print("PARENT: {} LEFT CHILD: {} RIGHT CHILD: {}".format(
                self.heap[i],
                left_value,
                right_value
            ))
            i += 1
            if i >= len(self.heap) or np.isnan(self.heap[i]):
                break


heap = Heap(33)
heap.insert(11)
heap.insert(12)
heap.insert(55)
heap.insert(24)
heap.insert(555)
heap.insert(22)
heap.insert(9)
heap.insert(20)
heap.insert(12)
heap.insert(550)
print(heap.heap)
heap.traverse()