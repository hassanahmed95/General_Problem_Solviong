# Find the middle element of a singly linked list  in one pass?
# Solution #1
# A simple way is to traverse all nodes of Linked list to get the length of the list and then in second pass
# traverse again to len/2 to get the middle number


# Solution #2
# start with two pointers from the head node. Onegit  pointer will traverse one node at time and second pointer
# will traverse two nodes at time. This way the faster pointer will reach the end of the list while the
# the second pointer will be halfway, so second pointer will be at mid of the list

class Node:
    def __init__(self, data, next):
        self.data = data
        self.next = next


n1 = Node("Hey", None)
n2 = Node("Python", n1)
n3 = Node("is", n2)
head = n3

# initially both pointer will be referring to head of the list
fastPointer = head
slowPointer = head

while fastPointer.next is not None and fastPointer.next.next is not None:
    fastPointer = fastPointer.next.next
    slowPointer = slowPointer.next
print(slowPointer.data)
