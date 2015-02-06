import copy


class BSTNode:
    def __init__(self, key, value) :
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
        

class BinarySearchTree :
    def __init__(self):
        self.root = None
        self.size = 0
    def findOps(self, key, node):
        if(self.root==None) :
            return self.root
        elif(node.key==key) :
            return node
        elif(node.key>key) :
            if(node.left==None) :
                return node
            else : 
                return self.findOps(key, node.left)
        elif(node.key<key) :
            if(node.right==None) :
                return node
            else : 
                return self.findOps(key, node.right)
            
    def find(self, key):
        return self.findOps(key, self.root)
        
    def first(self):
        node = self.root
        while(node.left!=None) :
            node = node.left
        return node
    
    def last(self):
        node = self.root
        while(node.right!=None) :
            node = node.right
        return node 
    
    def insert(self, key, value):
        entry = BSTNode(key,value)
        if(self.root==None) :
            self.root = entry
        else :
            parent = self.find(key)
            entry.parent = parent
            if(parent.key>=key) :
                parent.left = entry
            else :
                parent.right = entry
        self.size = self.size + 1
        return entry
    
    def removeOps(self, key, targetNode):
        node = self.findOps(key, targetNode)
        if(node.parent.key==key) :
            if(node.parent.left.key==key) :
                node.parent.left = None
            else :
                node.parent.right = None
        elif(node.parent.key>key) :
            node.parent.left = None
        else :
            node.parent.right = None
        if(node.left==None and node.right==None) :
             node.parent = None
        elif(node.left!=None and node.right!=None) :
            newNode = copy.deepcopy(self.findOps(node.key,node.right))
            self.size += 1
            newNode.parent=node.parent
            if(node.parent.key<=node.key) :
                node.parent.right = newNode
            else :
                node.parent.left = newNode
            newNode.left = node.left
            newNode.right = node.right
            newNode.right.parent = newNode
            self.removeOps(newNode.key, newNode.right)
        else :
            if(node.left!=None) :
                node.left.parent = node.parent
            else :
                node.right.parent = node.parent
            node.parent = None
        node.right = None
        node.left = None
        self.size = self.size - 1
        return node
    
    def remove(self,key):
        self.removeOps(key, self.root)
        
    def inOrderOps(self,node):
        if(node.left!=None) :
            self.inOrderOps(node.left)
        print(node.key, " : ", node.value)
        if(node.right!=None) :
            self.inOrderOps(node.right)
    def inOrder(self):
        self.inOrderOps(self.root)
        

tree = BinarySearchTree()
tree.insert(50, "Hello")
tree.insert(25, "Nice to Meet You")
tree.insert(13, "What's your Name?")
tree.insert(43, "How Are You?")
tree.insert(75, "Good Evening")
tree.insert(100, "Good Night!")
print("first", tree.first().key)
print("last", tree.last().key)
tree.remove(25)
print(tree.size)
tree.inOrder()

