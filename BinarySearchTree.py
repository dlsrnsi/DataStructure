'''
Binary Search Tree
Ordered dictionary : dictionary is which keys have a total, like a heap
Quickly find entry with minimum or maximum key, or entry nearest another entry

Binary Search Tree invariant :
    for any node X, every key in left subtree of x is <= X's key
                    every key in right subtree of x is >= X's key
Inorder traversal of a binary search tree visits nodes in sorted order

1. Entry find(Object key)
    How to find smallest key >= or largest key <=k
    When Searching down tree for a key k that is not in tree, we encounter both node
    containing smallest key > k and node containing largest key < k

2. Entry first(), Entry last()
    first() : If tree is empty, return null, otherwise, start at root.
              Repeatedly, go to left child until reach a node with no left child
    last()  : Do a reverse of first()

3. Entry insert(Object k, Object v)
    Follow same path through tree as find(), when you reach null reference,
    replace null with new node with Entry(k,v)
    Duplicate keys allowed, puts new entry in left subtree of old one \
    ## this implementation can't insert duplicate keys

4.Entry remove(Object k)
    Find a node n with key k, Return null if k not in tree
        *if n has no children, detach it from parent
        * If n has one child, move n's child up to take n's place
        * If n has 2 children, Let x be node n's right subtree with the smallest key.
          Remove x - x has no left child and is easily removed - Replace key with x's key
'''


class BSTNode:
    def __init__(self, key, value) :
        self.key = key
        self.value = value
        self.parent = None
        self.left = None
        self.right = None
    def hasBothChild(self) :
        if self.right and self.left :
            return True
        else : return False
    def hasOneChild(self) :
        if (self.right or self.left) and not self.hasBothChild() :
            return True
        else : return False
    def hasNoChild(self) :
        if not self.left and not self.right :
            return True
        else : return False
    def isLeft(self) :
        if not self.parent :
            return False
        if self.parent.left == self :
            return True
        else : return False
    def isRight(self) :
        if not self.parent :
            return False
        if self.parent.right == self :
            return True
        else : return False

class BinarySearchTree :
    def __init__(self):
        self.root = None
    def findOps(self, key, node):
        if node.key==key :
            return node
        elif node.key>key :
            if node.left :
                return self.findOps(key, node.left)
            else :
                return node
        elif node.key<key :
            if node.right  :
                return self.findOps(key, node.right)
            else :
                return node

    def find(self, key):
        if self.root == None :
            print("Tree is empty. Nothing to find")
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

    def insertOps(self, entry, node):
        parent = self.findOps(entry.key, node)
        if parent.key>entry.key :
            if not parent.left :
                parent.left = entry
                entry.parent = parent
            else :
                 return self.insertOps(entry, parent.left)
        elif parent.key<entry.key :
            if not parent.right :
                parent.right = entry
                entry.parent = parent
            else :
                return self.insertOps(entry, parent.right)
        return entry

    def insert(self,key, value):
        entry = BSTNode(key,value)
        if self.root == None :
            print("root : ", entry.key, entry.value)
            self.root = entry
        return self.insertOps(entry,self.root)

    def removeOps(self, key, node):
        target = self.findOps(key,node)
        if target.key == key :
            print(target.key, target.value,target.left,target.right)
            if target.hasNoChild() :
                print("hasNoChild")
                self.newLinkwithParent(target, None)
            elif target.hasBothChild() :
                print("hasBothChild")
                newNode = self.findOps(key, target.right)
                if newNode.hasOneChild() :
                    newNode.right.parent = newNode.parent
                    newNode.parent.left = newNode.right
                self.newLinkwithParent(target,newNode)
                newNode.parent = target.parent
                newNode.left = target.left
                newNode.right = target.right
                newNode.left.parent = newNode
                newNode.right.parent = newNode
            elif target.hasOneChild() :
                print("hasOneChild")
                if target.left :
                    child = target.left
                else :
                    child = target.right
                child.parent = target.parent
                self.newLinkwithParent(target,child)

            target.left = None
            target.right = None
        else :
            return None
    def newLinkwithParent(self,node,newNode):
        if node.isLeft() :
            node.parent.left = newNode
        else :
            node.parent.right = newNode
        node.parent = None

    def remove(self,key):
            self.removeOps(key, self.root)

    def inOrderOps(self,node):
            if(node.left!=None) :
                self.inOrderOps(node.left)
            print(node.key, " : ", node.value, end="")
            if node.isLeft() :
                print("is Left Child")
            elif node==self.root :
                print("is Root")
            else :
                print("is Right Child")
            if(node.right!=None) :
                self.inOrderOps(node.right)
            self.size +=1
    def inOrder(self):
        self.size = 0
        self.inOrderOps(self.root)
        print("size : ",self.size)
