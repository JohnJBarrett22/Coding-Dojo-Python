class Node:
    def __init__(self, value):
        self.value = value
        self.next =  None

class SList:
    def __init__(self, value):
        node = Node(value)
        self.head = node

    def addNode(self, value):
        node = Node(value)
        runner = self.head
        while(runner.next != None):
            runner = runner.next
        runner.next = node

    def printAllValues(self):
        runner = self.head
        print("Head points to " + str(id(self.head))+".")
        print("Printing the node id, value and following node's id:")
        while(runner.next != None):
            print(id(runner), runner.value, id(runner.next))
            runner = runner.next
        print(id(runner), runner.value, id(runner.next))

    def removeNode(self, value):        
        if(self.head != None):
            if(self.head.value == value):
                self.head = self.head.next
                return
            runner = self.head
            while(runner.next != None):
                if(runner.next.value == value):
                    runner.next = runner.next.next
                else:
                    runner = runner.next

    def insertNode(self, value, index):
        node = Node(value)
        if index == 0:
            node.next = self.head
            self.head = node
        else:
            count = 0
            runner = self.head
            while runner.next != None and count < index:
                count += 1
                if(count == index):
                    node.next = runner.next
                    runner.next = node
                runner = runner.next


mylist = SList(5)
mylist.addNode(7)
mylist.addNode(9)
mylist.insertNode(11,1)
mylist.insertNode(8,3)
mylist.addNode(4)
mylist.addNode(1)   
mylist.printAllValues()
mylist.removeNode(9)
mylist.removeNode(5)
mylist.removeNode(1)
mylist.printAllValues()
