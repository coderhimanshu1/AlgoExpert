# Do not edit the class below except for
# the insert, contains, and remove methods.
# Feel free to add new properties and methods
# to the class.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


    def insert(self, value):
        currentNode=self
        while currentNode is not None:
            if value < currentNode.value:
                if currentNode.left:
                    currentNode = currentNode.left
                else:
                    currentNode.left = BST(value)
                    break
            else:
                if currentNode.right:
                    currentNode = currentNode.right
                else:
                    currentNode.right = BST(value)
                    break
        return self


    def contains(self, value):
        
        currentNode = self


        while currentNode is not None:
            if value == currentNode.value: 
                return True
            elif value < currentNode.value:
                currentNode = currentNode.left