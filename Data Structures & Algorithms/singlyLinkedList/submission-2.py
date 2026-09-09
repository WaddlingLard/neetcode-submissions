class Node:
    def __init__(self, value):
        self.val = value
        self.next = None

class LinkedList:
    
    def __init__(self):
        self.size = 0
        self.head: Node = None
        self.tail: Node = None
    
    def get(self, index: int) -> int:
        if self.size - 1 < index:
            return -1

        print('get!')
        
        node_ptr: Node = self.head
        iterator: int = 0
        while iterator != index:
            iterator += 1
            node_ptr = node_ptr.next

        return node_ptr.val

    def insertHead(self, val: int) -> None:
        new_head_node: Node = Node(val)
        self.size += 1

        if self.size == 1:
            self.head = self.tail = new_head_node
        else:
            new_head_node.next = self.head
            self.head = new_head_node

    def insertTail(self, val: int) -> None:
        new_tail_node: Node = Node(val)
        self.size += 1
        
        if self.size == 1:
            self.tail = self.head = new_tail_node
        else:
            self.tail.next = new_tail_node
            self.tail = new_tail_node

    def remove(self, index: int) -> bool:
        if self.size - 1 < index:
            return False
        
        self.size -= 1
        if self.size == 0:
            # The linked list is now empty
            self.head = self.tail = None
        elif index == 0:
            # Removing the head
            self.head = self.head.next
        else:
            # The node removed will be later in the linked list
            node_ptr: Node = self.head
            iterator: int = 0
            while iterator != index - 1:
                iterator += 1
                node_ptr = node_ptr.next
            node_to_delete: Node = node_ptr.next
            if node_to_delete == self.tail:
                node_ptr.next = None
                self.tail = node_ptr
            else:
                node_ptr.next = node_to_delete.next
        
        return True

    def getValues(self) -> List[int]:
        values: list[int] = []
        node_ptr: Node = self.head
        while node_ptr:
            values.append(node_ptr.val)
            node_ptr = node_ptr.next
        return values