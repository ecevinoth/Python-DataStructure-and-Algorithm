
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


def cycle_check(node):
    marker1 = node
    marker2 = node

    while marker2.next is not None and marker2.next.next is not None:
        marker1 = marker1.next
        marker2 = marker2.next.next

        if marker1 == marker2:
            return True
    return False

a = Node(1)
b = Node(2)
c = Node(3)

a.next = b
b.next = c
c.next = a

print(cycle_check(a))
