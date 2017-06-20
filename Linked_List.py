class Node():
    def __init__(self,data):
        self.data=data
        self.next=None
    def getdata(self):
        return self.data
    def getnext(self):
        return self.next
    def setdata(self,ndata):
        self.data=ndata
    def setnext(self,nnext):
        self.next=nnext
class Linked_List():
    def __init__(self):
        self.head=None
    def create_node(self,data):
        if self.head==None:
            self.head=Node(data)
        else:
            self.add_end(data)
    def add_beg(self,data):
        current_node=self.head
        new_node=Node(data)
        new_node.setnext(current_node)
        self.head=new_node
    def add_end(self,data):
        current_node=self.head
        while(current_node.getnext()!=None):
            current_node=current_node.getnext()
        new_node=Node(data)
        current_node.setnext(new_node)
    def delete(self,data):
        current=self.head
        prev=None
        while current!=None:
            if current.getdata()==data:
                if current==self.head:
                    self.head=self.head.getnext()
                else:
                    prev.setnext(current.getnext())
            else:
                prev=current
            current=current.getnext()
    def del_loc(self,loc):
        current=self.head
        count=1
        while count<loc and loc>1:
            prev=current
            current=current.getnext()
            count=count+1
        prev.setnext(current.getnext())
    def sortinsert(self,data):
        current=self.head
        prev=None
        while current.getdata()<data:
            prev=current
            current=current.getnext()
        newnode=Node(data)
        newnode.setnext(current)
        prev.setnext(newnode)
    def reverse(self):
        current=self.head
        prev=None
        while current!=None:
            nextN=current.getnext()
            current.setnext(prev)
            prev=current
            current=nextN
        self.head=prev
    def display(self):
        current=self.head
        while(current!=None):
            print(current.getdata(),end='->')
            current=current.getnext()
LL=Linked_List()
LL.create_node(1)
LL.create_node(2)
LL.create_node(4)
LL.create_node(5)
LL.add_beg(9)
LL.display()
LL.delete(9)
print('\n')
LL.display()
print('\n')
LL.del_loc(2)
LL.display()
print('\n')
LL.sortinsert(3)
LL.display()
LL.reverse()
print('\n')
LL.display()
