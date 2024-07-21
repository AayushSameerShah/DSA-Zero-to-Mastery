'''
Here we will implement the LinkedList in python.
This is going to be easy. Keep calm.
'''

class LinkedList:
    def __init__(self, value):
        self.head = {"value": value,
                     "next": None}
        self.tail = self.head
        self.length = 1

    def append(self, value):
        node = {"value": value, "next": None}
        self.tail["next"] = node
        self.tail = node
        self.length += 1

    def prepend(self, value):
        node = {"value": value, "next": None}
        node["next"] = self.head
        self.head = node
        self.length += 1

    def insert(self, index, value):
        if index >= self.length or index <= 0:
            raise IndexError("The index is invalid.")
        
        pointer = self.head
        for idx in range(1, index):
            pointer = pointer["next"]

        node = {"value": value, "next": pointer["next"]}
        pointer["next"] = node
        self.length += 1

    def delete(self, index):
        if index >= self.length or index < 0:
            raise IndexError("The index is invalid.")
        
        pointer = self.head
        for idx in range(1, index):
            pointer = pointer["next"]
        
        pointer["next"] = pointer["next"]["next"]
        self.length -= 1

    def reverse_by_values(self):
        '''
        This is my implementation when I didn't understand 
        the instructions well.
        
        Here, I just swap the values from first to last.
        The nodes direct the same way as they did.
        
        The **actual** implementation is implemented below.
        '''
        pointer = self.head
        locations = [pointer]
        for _ in range(1, self.length):
            pointer = pointer["next"]
            locations.append(pointer)
        
        till = self.length // 2
        for th in range(till):
            locations[self.length-1-th]["value"], locations[th]["value"] = locations[th]["value"], locations[self.length-1-th]["value"]
            
        print("Reversal successful.")

    def reverse_list(self):
        '''
        This is the actual implementation of "what the reverse LL
        would look like".
        '''
        if self.length == 1:
            return None
        else:
            first = self.head
            second = first["next"]
            
            while (second):
                temp = second["next"]
                second["next"] = first
                first = second
                second = temp

            self.head, self.tail = self.tail, self.head
            self.tail["next"] = None                

        

    def visualize(self):
        if not self.head and not self.tail:
            raise NotImplementedError("The LL is empty.")

        print(self.head["value"], end="-->")
        here = self.head["next"]
        while here:
            print(here["value"], end="-->")
            here = here["next"]
        else:
            print("End of list")


first = LinkedList(value=11)
# first.append(12)
# first.append(13)
# first.append(14)
# first.append(15)
# first.append(16)
first.visualize()

# first.reverse_by_values()
first.reverse_list()
first.visualize()