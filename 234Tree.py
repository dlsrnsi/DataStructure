'''
Created on 2015. 2. 5.

@author: Ingoo
'''
class Entry :
    def __init__(self, key, value) :
        self.key = key
        self.value = value

class Node : 
    def __init__(self):
        self.parent = None
        self.entryList = []
        self.numOfEntry = 0
        self.childList = []
        self.numOfChild = 0

class Two_Four_Tree :
    def __init__(self):
        self.root = None
        
    def find(self, key):
        if(self.root == None) :
            return None
        else :
            return self.findOps(key,self.root)
    
    def findOps(self, key, node):
        a = 0
        for x in node.entryList :
            if(x.key==key) :
                return x , a, node
            elif(x.key>key) :
                if(len(node.childList)==0) :
                    return x , a, node
                else :
                    return self.findOps(key, node.childList[a])
            a += 1
        else :
            if(len(node.childList)==0) :
                    return node.entryList[a], a, node
            else :
                    return self.findOps(key, node.childList[a])
    
    def insert(self, key, value):            
        node = Node()
        node.entryList.append(Entry(key, value))
        if(self.root==None) :
            self.root = node
        else :
            parentTuple = self.find(key)
            if(len(parentTuple[2].entryList)==3) :
                pass
            else :
                parentTuple[2].childList.insert(parentTuple[1], node)
                node.parent = parentTuple[2]
    
    def split(self, node):
        pass
    
    def remove(self, key):
        pass
    
            


tree = Two_Four_Tree()
tree.insert(50, "Hello")
print(tree.root.entryList, tree.root.childList)
tree.insert(25, "Hi")
print(tree.root.entryList, tree.root.childList)