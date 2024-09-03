class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
def linear_search(head, target):
    current = head
    position = 0
    while current:
        if current.data == target:
            return position
        current = current.next
        position += 1
    return None
head = Node(3)
head.next = Node(7)
head.next.next = Node(10)
print(linear_search(head, 7))
