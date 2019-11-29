class Node:
    def __init__(self, value):
        self.value = value
        self.nextnode = None
        

def nth_to_lastnode(n, head):
    left_pointer = head
    right_pointer = head
    
    for i in range(n-1):
        if right_pointer.nextnode is None:
            raise LookupError("n is greater than the linked list")
        right_pointer = right_pointer.nextnode

    while right_pointer.nextnode:
        left_pointer = left_pointer.nextnode
        right_pointer = right_pointer.nextnode
    return left_pointer.value

a = Node(1)
b = Node(2)
c = Node(3)
d = Node(4)

a.nextnode = b
b.nextnode = c
c.nextnode = d
d.nextnode = None

print(nth_to_lastnode(3,a))
