# Creating a Node
class Node:
    def __init__(self, next=None, prev=None, data=None):
        self.next = next  
        self.prev = prev  
        self.data = data

# Adding a node at the front of the list
class DoublyLinkedList:
    def insertFront(self, new_data):
        new_node = Node(data=new_data)
        new_node.next = self.head
        new_node.prev = None

        if self.head is not None:
            self.head.prev = new_node

        self.head = new_node


    def insertAfter(self, prev_node, new_data):
        if prev_node is None:
            print("This node doesn't exist in DLL")
            return
        new_node = Node(data=new_data)
        new_node.next = prev_node.next
        prev_node.next = new_node
        new_node.prev = prev_node
        if new_node.next is not None:
            new_node.next.prev = new_node


    def append(self, new_data):
        new_node = Node(data=new_data)
        last = self.head
        new_node.next = None
        if self.head is None:
            new_node.prev = None
            self.head = new_node
            return
        while (last.next is not None):
            last = last.next
        last.next = new_node
        new_node.prev = last


    def printList(self, node):
        print("\nTraversal in forward direction")
        while(node is not None):
            print (" % d" % (node.data))
            last = node
            node = node.next

        print ("\nTraversal in reverse direction")
        while(last is not None):
            print (" % d" % (last.data))
            last = last.prev


llist = DoublyLinkedList()
llist.append(6)
llist.insertFront(7)
llist.insertFront(1)
llist.append(4)
llist.insertAfter(llist.head.next, 8)
print("Created DLL is: ")
llist.printList(llist.head)

