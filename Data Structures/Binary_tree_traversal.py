class Stack:
     def __init__(self):
         self.items = []

     def empty(self):
         return self.items == []

     def push(self, item):
         self.items.append(item)

     def pop(self):
         return self.items.pop()

     def peek(self):
         return self.items[len(self.items)-1]

     def size(self):
         return len(self.items)
     
class Queue:
    def __init__(self):
        self.items = []

    def empty(self):
        return self.items == []

    def put(self, item):
        self.items.insert(0,item)

    def get(self):
        return self.items.pop()

    def size(self):
        return len(self.items)

class Node():
    def __init__(self,data):
        self.data=data
        self.left=None
        self.right=None
    def setdata(self,ndata):
        self.data=ndata
    def getdata(self):
        return self.data
    def getleft(self):
        return self.left
    def getright(self):
        return self.right
    def setleft(self,ldata):
        self.left=ldata
    def setright(self,rdata):
        self.right=rdata
class Binary_Tree():
    def __init__(self):
        self.root=None
        return self.root
    def getroot(self):
        return self.root
    def add(self,data):
        if self.root==None:
            self.root=Node(data)
        else:
            self.add_helper(self.root,data)
    def add_helper(self,root,data):
        if data<root.getdata():
            if root.getleft()is None:
                root.setleft(Node(data))
            else:
                self.add_helper(root.getleft(),data)
        elif data>root.getdata():
            if root.getright() is None:
                root.setright(Node(data))
            else:
                self.add_helper(root.getright(),data)
    def preorder(self):
        self.preorder_helper(self.root)
        print('\n')
    def preorder_helper(self,root):
        if root is not None:
            print (root.getdata(),end='->')
            self.preorder_helper(root.getleft())
            self.preorder_helper(root.getright())
    def postorder(self):
        self.postorder_helper(self.root)
        print ('\n')
    def postorder_helper(self,root):
        if root is not None:
            self.postorder_helper(root.getleft())
            self.postorder_helper(root.getright())
            print (root.getdata(),end='->')
    def Inorder(self):
        self.Inorder_helper(self.root)
        print ('\n')
    def Inorder_helper(self,root):
        if root is not None:
            self.Inorder_helper(root.getleft())
            print (root.getdata(),end='->')
            self.Inorder_helper(root.getright())
    def levelorder(self):
        if self.root is not None:
            self.levelorder_helper(self.root)
    def levelorder_helper(self,root):
        result=[]
        node=None
        q=Queue()
        q.put(root)
        while not q.empty():
            node=q.get()
            result.append(str(node.getdata()))
            if node.getleft() is not None:
                q.put(node.getleft())
            if node.getright() is not None:
                q.put(node.getright())
        print ('->'.join(result))
    def findmax(self):
        if self.root is not None:
            print(self.findmax_helper(self.root))
    def findmax_helper(self,root):
        maxd=0
        node=None
        q=Queue()
        q.put(root)
        while not q.empty():
            node=q.get()
            if node.getdata()>maxd:
                maxd=node.getdata()
            if node.getleft() is not None:
                q.put(node.getleft())
            if node.getright() is not None:
                q.put(node.getright())
        return maxd
    def search(self,data):
        if self.root is not None:
            self.search_helper(self.root,data)
    def search_helper(self,root,data):
        if root is not None:
            if root.getdata()==data:
                print('found')
                return 1
            else:
                temp=self.search_helper(root.getleft(),data)
                tmp=self.search_helper(root.getright(),data)
                if temp==1 or tmp==1:
                    print ('found')           
    def insert(self,data):
        if self.root is not None:
            self.insert_helper(self.root,data)
    def insert_helper(self,root,data):
        nn=Node(data)
        if data>root.getdata():
            if root.getright() is None:
                root.setright(nn)
            else:
                self.insert_helper(root.getright(),data)
        else:
            if root.getleft() is None:
                root.setleft(nn)
            else:
                self.insert_helper(root.getleft(),data)
    def findsize(self):
        if self.root is not None:
            print (self.findsize_helper(self.root))
    def findsize_helper(self,root):
        if root is None:
            return 0
        return self.findsize_helper(root.getleft())+self.findsize_helper(root.getright())+1
    def findsize_nonrecursive(self):
        if self.root is not None:
            print (self.findsize_nonrecursive_helper(self.root))
    def findsize_nonrecursive_helper(self,root):
        node=None
        q=Queue()
        q.put(root)
        count=0
        while not q.empty():
            node=q.get()
            count=count+1
            if node.getleft() is not None:
                q.put(node.getleft())
            if node.getright() is not None:
                q.put(node.
                      getright())
        return count
    def reverseLevelOrder(self):
        if self.root is not None:
            self.reverseLevelOrder_helper(self.root)
    def reverseLevelOrder_helper(self,root):
        if root is not None:
            q=Queue()
            s=Stack()		
            node=None
            q.put(root)
            while not q.empty():
                node=q.get()
                if node.getleft() is not None:
                    q.put(node.getleft())
                if node.getright() is not None:
                    q.put(node.getright())
                s.push(node.getdata())
        while (not s.empty()):
            print(s.pop(),end='->')
        print('\n')

B=Binary_Tree()
B.add(1)
B.add(2)
B.add(3)
B.add(4)
B.add(5)
B.add(6)
B.add(7)
print('Preorder Traversal:')
B.preorder()
print('Inorder Traversal:')
B.Inorder()
print('Postorder Traversal:')
B.postorder()
print('Levelorder Traversal:')
B.levelorder()
print('Max value:')
B.findmax()
print('Search 1:')
B.search(1)
print('Insert 8')
B.insert(8)
print('Levelorder Display:')
B.levelorder()
print('Find size:')
B.findsize()
print('FInd size using nonrecursive method:')
B.findsize_nonrecursive()
print('Levelorder Display:')
B.levelorder()
