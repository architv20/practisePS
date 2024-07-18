class Node:
    def __init__(self,data=None,next=None):
        self.data = data
        self.next = next

class LinkedList:
    def __init__(self):
        self.head = None

    def insertAtBeginning(self,data):
        nd = Node(data,self.head)
        self.head = nd
    
    def insertAtEnd(self,data):
        nd = Node(data,None)
        last = False
        if self.head == None:
            self.head = nd
            last = True
        itr = self.head
        while last == False:
            if itr.next == None:
                itr.next = nd
                last = True
            else:
                itr = itr.next
    
    def insertAfter(self,data,after):
        itr = self.head
        move = True
        while move:
            if itr.data == after:
                nd = Node(data,itr.next)
                itr.next = nd
                move = False
            else:
                itr = itr.next
    
    def insertBefore(self,data,before):
        itr = self.head
        move = True
        if itr.data == before:
            nd = Node(data,itr)
            self.head = nd
            move = False
        while move:
            if itr.next.data == before:
                nd = Node(data,itr.next)
                itr.next = nd
                move = False
            else:
                itr = itr.next

    def insertValues(self,values):
        for i in values:
            self.insertAtEnd(i)

    def removeAt(self,index):
        itr = self.head
        cnt = 0
        move = True
        while move:
            if cnt == index - 1:
                itr.next =  itr.next.next
                move = False
            else:
                cnt += 1
                itr = itr.next

    def removeValue(self,data):

    def insertAt(self,data, )
    def length(self):
        if self.head == None:
            print(0)
        else:
            cnt = 1
            itr = self.head
            while itr.next != None:
                cnt += 1
                itr = itr.next
            print(cnt)

    def print(self):
        itr = self.head
        str = ''
        while itr != None:
            str += itr.data + '-->'
            itr = itr.next
        print (str)

if __name__ == "__main__":
    ll = LinkedList()
    ll.print()

    ll.insertAtEnd("Will")
    ll.print()

    ll.insertAtBeginning("Harsha")
    ll.print()

    ll.insertAtBeginning("Archit")
    ll.print()

    ll.insertAtEnd("Shaadi")
    ll.print()

    ll.insertAfter("Will","Archit")
    ll.print()

    ll.insertBefore("Is","Harsha")
    ll.print()

    ll.insertBefore("Awesome","Will")
    ll.print()

    ll.insertBefore("Awesome","Archit")
    ll.print()

    l2 = LinkedList()

    l2.insertValues(["Archit","Loves","Harsha","a","lot"])
    l2.print()

    l2.removeAt(2)
    l2.print()

    l2.length()

    ll.length()
