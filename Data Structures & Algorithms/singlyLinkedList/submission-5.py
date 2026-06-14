class Node:
    def __init__(self, val, next_node=None):
        self.val = val
        self.next_node = next_node


class LinkedList:
    
    def __init__(self):
        self.head = None

    
    def get(self, index: int) -> int:
        curr = self.head
        curr_idx = 0

        while curr is not None and curr_idx < index:
            curr = curr.next_node
            curr_idx += 1
        
        if curr is None:
            return -1
        
        return curr.val
        

    def insertHead(self, val: int) -> None:
        self.head = Node(val, self.head)


    def insertTail(self, val: int) -> None:
        if self.head is None:
            self.head = Node(val)
            return

        curr = self.head

        while curr.next_node is not None:
            curr = curr.next_node
        
        curr.next_node = Node(val)
        

    def remove(self, index: int) -> bool:
        curr = self.head
        prev = None
        curr_idx = 0

        while curr is not None and curr_idx < index:
            prev = curr
            curr = curr.next_node
            curr_idx += 1
        
        if curr is None:
            return False
        
        if prev is None:
            self.head = curr.next_node
            return True
        
        prev.next_node = curr.next_node

        return True
        

    def getValues(self) -> List[int]:
        res = []
        curr = self.head

        while curr is not None:
            res.append(curr.val)
            curr = curr.next_node
        
        return res
        
