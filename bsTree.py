class BinaryNode:
    def __init__(self,value):
        self.value = value
        self.left = None
        self.right = None
        
    def add(self,val):
        if val <= self.value :
            self.left = self.addToSubTree(self.left, val)
        elif val > self.value:
            self.right = self.addToSubTree(self.right, val)
    def addToSubTree(self, parent,value):
        if parent is None:
            return BinaryNode(value)
        parent.add(value)
        return parent

        
class BinaryTree:
    def __init__(self):
        self.root = None
        
    def add(self, value):
        if self.root == None:
            self.root = BinaryNode(value)
        else:
            self.root.add(value)
    
    def remove(self, value):
        pass
    
    def __contains__(self, target):
        node = self.root 
        while node is not None:
            if node.value < target:
                node = node.right
            elif node.value > target:
                node = node.left 
            else:
                return True  
            
        return False  
    
    
    
    