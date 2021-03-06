class node:
    def __init__(self,data):
        self.data = data
        self.next = None
class linkedList:
    def __init__(self):
        self.head = None
    def insertAtStart(self,data):
        temp = node(data)
        if self.head is None:
            self.head = temp
        else:
            temp.next = self.head
            self.head = temp
    def display(self):
        temp = self.head
        i=1
        while temp is not None:
            print("data is {0} node is {1}".format(i,temp.data))
            i = i+1
            temp = temp.next
    def returnNodeAtPos(self,pos):
        temp = self.head
        if pos is 1:
            return temp
        else:
            for i in range(1,pos):
                temp = temp.next
        return temp
    def LengthLinkedListIterative(self):
        temp = self.head
        count = 0
        while temp:
            count = count+1
            temp = temp.next
        return count

    def detetcALoopInsideLinkedListWithNoOfNodes(self,len):
        temp = self.head
        tempcount = 1;
        while temp:

            if tempcount>len:
                print("There is a loop")
                return
            temp = temp.next
            tempcount = tempcount+1
        print("There is no loop")

if __name__=='__main__':
    ll = linkedList()
    ll.insertAtStart(10)
    ll.insertAtStart(11)
    ll.insertAtStart(12)
    ll.insertAtStart(13)
    ll.insertAtStart(14)
    ll.insertAtStart(15)
    ll.display()
    nodeat3 = ll.returnNodeAtPos(3)
    nodeatlast = ll.returnNodeAtPos(6)
    print("data inside the node at posotion 3 is {0} and inside the last node is {1}".format(nodeat3.data,nodeatlast.data))
    #before we make a loop in it get the length of the linked list
    lenofll = ll.LengthLinkedListIterative()
    #now make the last node to point the 3 rd node

    nodeatlast.next = nodeat3
    print("data inside the node after last node is :",nodeatlast.next.data,"this is the start of the loop")

    #now detecting a loop is present or not
    ll.detetcALoopInsideLinkedListWithNoOfNodes(lenofll)