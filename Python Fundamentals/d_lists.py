class Node:
    def __init__(self, value):
        self.value = value
        self.next =  None
        self.prev = None

class DoublyLinkedList:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNodeAppend(self, value):
        if(self.head is None):
            node = Node(value)
            node.prev = None
            self.head = node
        else:
            node = Node(value)
            runner = self.head
            while(runner.next):
                runner = runner.next
            runner.next = node
            node.prev = runner   
        
    def addNodePrepend(self, value):
        if(self.head is None):
            node = Node(value)
            node.prev = None
            self.head = node
        else:
            node = Node(value)
            self.head.prev = node
            node.next = self.head
            self.head = node
            node.prev - None

    def removeNode(self, value):
        runner = self.head
        while runner:
            if(runner.value == value and runner == self.head):
                if(not runner.next):
                    runner = None
                    self.head = None
                    return
                else:
                    temp = runner.next
                    runner.next = None
                    temp.prev = None
                    runner = None
                    self.head = temp
                    return
            elif runner.value == value:
                if runner.next:
                    temp = runner.next
                    prev = runner.prev
                    prev.next = temp
                    temp.prev = prev
                    runner.next = None
                    runner.prev = None
                    runner = None
                    return
                else:
                    prev = runner.prev
                    prev.next = None
                    runner.prev = None
                    runner = None
                    return
            runner = runner.next

    def insertNodeAfter(self, value, key):
        runner = self.head
        while runner:
            if(runner.next is None and runner.value == key):
                self.addNodeAppend(value)
                return
            elif(runner.value == key):
                node = Node(value)
                temp = runner.next
                runner.next = node
                node.next = temp
                node.prev = runner
                temp.prev = node
            runner = runner.next

    def insertNodeBefore(self, value, key):
        runner = self.head
        while runner:
            if(runner.prev is None and runner.value == key):
                self.addNodePrepend(value)
                return
            elif(runner.value == key):
                node = Node(value)
                prev = runner.prev
                prev.next = node
                runner.prev = node
                node.next = runner
                node.prev = prev
            runner = runner.next

    def printAllValues(self):
        runner = self.head
        print("Head points to " + str(id(self.head))+".")
        print("Value / Previous / Current / Next:")
        while(runner.next != None):
            print(runner.value, id(runner.prev), id(runner), id(runner.next))
            runner = runner.next
        print(runner.value, id(runner.prev), id(runner), id(runner.next))


mylist = DoublyLinkedList(5)
mylist.addNodeAppend(7)
mylist.addNodeAppend(4)
mylist.addNodeAppend(9)
mylist.addNodeAppend(1)   
mylist.printAllValues()
mylist.removeNode(1)
mylist.printAllValues()
mylist.insertNodeAfter(3,9)
mylist.printAllValues()
mylist.insertNodeBefore(8,7)
mylist.printAllValues()
