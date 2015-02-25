__author__ = 'Ingoo'

'''
SPlay Tree
Balanced Binary Search
All Operations : O(long(n)) time average
Single Operation : O(n) worst-case time, where n is # of items in tree
Any sequence of k ops starting from empty tree, never >n items in tree,
O(klog(n)) worst-case time
Fast access to entries accessed recently

Tree Rotations
Splay trees are kept balanced with rotation
Splay trees are not kept perfectly balanced

Splay Tree Operation

1. Object find(object k)
    Begin like in ordinary BST. Walk down tree to key k ordered.
    Let X be node where search ended whether it contains k or no not.
    Splay X up tree through a sequence of rotations, so X becomes root.
    3 cases
        1. X is left child of right child OR right child of Left child.
        2. X is left child of left child Or right child of right child.
        3. X is child of the root

2. Object first(), Object last()
    Find entry with min/max key, splay it to root

3. void insert(Object k Object v)
    Insert new entry(k,v), Splay new node to the root

4. Object remove(Object K)
    An entry having key k, removed from tree, as with ordinary BST,
    Let X be the node remove from the tree. Splay X's parent to root.
    If key k is not in tree, splay the last node where the search ended
'''
import BinarySearchTree as BST

class SplayTree(BST.BinarySearchTree) :

    def zig(self,node):
        pass




    def splay(self,node):
        if node.parent==self.root :
            print("zig")
            self.zig(node)
            self.root = node
        elif node.isLeft() :
            if node.parent.isLeft() :
                #zig-zig
                print("zig-zig left left")
                self.zig(node.parent)
                self.zig(node)
            else :
                print("zig-zag left right")
                #zig-zag
                self.zig(node)
                self.zig(node.parent)
        elif node.isRight() :
            if node.parent.isRight() :
                print("zig-zig right right")
                #zig-zig
                self.zig(node.parent)
                self.zig(node)
            else :
                print("zig-zag right left")
                self.zig(node)
                self.zig(node.parent)

    def find(self, key):
        x = self.findOps(key,self.root)
        while x != self.root :
            self.splay(x)

    def insert(self, key, value):
        entry = BST.BSTNode(key,value)
        if not self.root :
            self.root = entry
        x = self.insertOps(entry,self.root)
        try : print("x key : ",x.key,", x dad key : ", x.parent.key)
        except AttributeError : print("root key : ",x.key)
        while x != self.root :
            self.splay(x)
            self.inOrder()
        return x


import random

tree = SplayTree()
list = random.sample(range(1, 100), 50)
print(list)
for x in list :
    tree.insert(x,x)
tree.inOrder()
