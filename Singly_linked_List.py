# Assignment
# Part 1 - recreate SList and Node.  Recreate addNode and printAllValues methods.
# Singly Linked List is one of the most fundamental data structures you'll be using.  Using the concepts here, you'll learn how to create other data structure such as Stacks, Queues, Doubly Linked List, Binary Search Trees, Tries, Graphs, etc.  As it's such a critical concept, please re-create the codes demonstrated above without looking at the platform.  Make sure you feel very comfortable with adding a new Node, traversing through the linked list, etc.  Once you can create both SList and Node without looking at the codes above, then proceed with Part 2.
# Part 2 - implement removeNode(val)
# Implement removeNode(val) where it removes a node with the value val.
# For example list.removeNode(5) will see if there's a node with the value of 5.  If it is, it will remove that from the linked list.
# When you do this, you'll need to consider the following cases:
# -when the node you want to remove is in the beginning of the linked list
# -when the node you want to remove is in the middle of the linked list
# -when the node you want to remove is at the end of the linked list
# For each of these cases, you will probably need to have different logics to handle the removal.

class Node:
    def __init__(self,value):
        self.value = value
        self.next = None

class SList:
    def __init__(self,value):
        node = Node(value)
        self.head = node

    def addNode(self,value):
        node = Node(value)
        runner = self.head
        while (runner.next != None):
            runner = runner.next
        runner.next = node


    def removeNode(self,val):
        runner = self.head
        if(runner != None):
            if(runner.value == val):
                self.head = runner.next
                runner = None
                return
        while(runner != None):
            if runner.value == val:
                break
            prev = runner
            runner = runner.next
        if(runner == None):
            return
        prev.next = runner.next
        runner = None


    def printAllValues(self, msg=""):
        runner = self.head
        print("\n\nhead points to", id(self.head))
        print("Printing the values in the list ---", msg, '---')
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
        print(id(runner), runner.value, id(runner.next))


print("\n\n\n\n================== START OF THE PROGRAM ================")
list = SList(5)
list.addNode(7)
list.addNode(9)
list.addNode(1)
list.removeNode(9)  # removes 9, which is one of the middle nodes in the list
list.removeNode(5)  # removes 5, which is the first value in the list
list.removeNode(1)  # removes 1, which is the last node in the list

list.printAllValues("Attempt 1")
