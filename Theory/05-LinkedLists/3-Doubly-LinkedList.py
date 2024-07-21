class DoublyLinkedList:
    def __init__(self, value) -> None:
        node = {"value":value, "prev":None, "next":None}
        self.head = node
        self.tail = self.head
        self.length = 1

    def append(self, value):
        node = {"value":value, "prev":self.tail, "next":None}
        self.tail["next"] = node
        self.tail = node
        self.length += 1
    
    def prepend(self, value):
        node = {"value":value, "prev":None, "next":self.head}
        self.head["prev"] = node
        self.head = node
        self.length += 1

    def insert(self, index, value):
        if index > self.length or index < 0:
            raise IndexError
        
        if index == 0:
            self.prepend(value=value)
        elif index == self.length:
            self.append(value=value)
        else:
            node = {"value":value, "prev":None, "next":None}
            side = round(index / self.length) # 0 if more on left else right
            if side == 0: # forward
                print("[INSERTING FROM LEFT]")
                pointer = self.head
                for _ in range(1, index):
                    pointer = pointer["next"]
                
                node["prev"] = pointer
                node["next"] = pointer["next"]
                pointer["next"]["prev"] = node
                pointer["next"] = node
            
            else: # backward
                print("[INSERTING FROM RIGHT]")
                pointer = self.tail
                for _ in range(self.length-1, index+1, -1):
                    pointer = pointer["prev"]
                
                pointer["prev"]["next"] = node
                node["prev"] = pointer["prev"]
                pointer["prev"] = node
                node["next"] = pointer

            self.length += 1

    def delete(self, index):
        if index >= self.length or index < 0:
            raise IndexError
        
        if index == 0:
            self.head = self.head["next"]
            self.head["prev"] = None
        elif index == self.length-1:
            self.tail = self.tail["prev"]
            self.tail["next"] = None
        else:
            side = round(index / self.length) # 0 if more on left else right
            if side == 0: # forward
                print("[DELETING FROM LEFT]")
                pointer = self.head
                for _ in range(1, index+1):
                    pointer = pointer["next"]
                
                pointer["prev"]["next"] = pointer["next"]
                pointer["next"]["prev"] = pointer["prev"]
            
            else: # backward
                print("[DELETING FROM RIGHT]")
                pointer = self.tail
                for _ in range(self.length-1, index+1, -1):
                    pointer = pointer["prev"]
                
                pointer["prev"]["next"] = pointer["next"]
                pointer["next"]["prev"] = pointer["prev"]
        self.length -= 1

    def visualize_from(self, forward=True):
        pointer = self.head if forward else self.tail
        if forward:
            while pointer:
                print("{} <-- {} --> {}".format(
                    pointer["prev"]["value"] if pointer["prev"] else None,
                    pointer["value"],
                    pointer["next"]["value"] if pointer["next"] else None
                ))
                pointer = pointer["next"]
        else:
            while pointer:
                print("{} <-- {} --> {}".format(
                    pointer["prev"]["value"] if pointer["prev"] else None,
                    pointer["value"],
                    pointer["next"]["value"] if pointer["next"] else None
                ))
                pointer = pointer["prev"]


LL = DoublyLinkedList(100)
LL.append(101)
LL.append(102)
print(LL.length)
LL.visualize_from(True)

LL.insert(2, 444)
print(LL.length)
LL.visualize_from(True)
LL.delete(3)
print(LL.length)
LL.visualize_from(True)