class queue:
    def __init__(self):
        self.x=[]
    def enqueue(self,arg):
        self.x=self.x+[arg]
        return True
    def dequeue(self):
        pop=self.x[0]
        self.x=self.x[1:len(self.x)]
        return pop
    def empty(self):
        if self.x==[]:
            return True
        else:
            return False
    def printList(self):
        print(self.x)
        return True

class tree:
    def __init__(self,x):
        self.store = [[x],[]]

    def AddSuccessor(self,x):
        self.store[1] = self.store[1] + [x]
        return True

    def addNodeVal(self,newVal):
        self.store[0]+=[newVal]
        return True
        
    def Print_DepthFirst(self):
        print(self.store[0])
        if self.store[1]==[]:
            return True
        else:
            for i in self.store[1]:
                i.Print_DepthFirst()
    
    def getSuccessors(self):
        return self.store[1]
    
    def getNode(self):
        return self.store[0]
    
    def Get_LevelOrder(self):
        ans=[]
        ans+=[self.store[0]]
        tQ=queue()
        tQ.enqueue(self.store[1])
        while tQ.empty()==False:
            out=tQ.dequeue()
            for i in out:
                ans+=[i.store[0]]
                tQ.enqueue(i.store[1])
        return ans    
    
    def getFirstLevel(self):
        ans=[]
        tQ=queue()
        tQ.enqueue(self.store[1])
        out=tQ.dequeue()
        for i in out:
            ans+=[i.store[0]]
        return ans
    def ConvertToBinaryTree(self):
        value=self.store[0]
        nodeList=self.store[1]
        newBTree=binary_tree(value)
        newTree.AddLeft(self.ConvertToBinaryHelper(nodeList))
        return newBTree

    def ConvertToBinaryHelper(self,nodeList):
        if nodeList!=[]:
            firstSib=nodeList[0]
            sibsList=nodeList[1:]
            newBTree=binary_tree(firstSib.store[0])
            newLeft=self.ConvertToBinaryHelper(firstSib.store[1])
            newRight=self.ConvertToBinaryHelper(sibsList)
            newBTree.AddLeft(newLeft)   
            newBTree.AddRight(newRight) 
            return newBTree
        else:
            return('NULL')
