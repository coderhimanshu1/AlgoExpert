def findClosestValueInBst(tree, target):
    # store closest value
    closest = tree.value


    # iterate over tree
    while tree is not None:


        # check if current value is closer to target
        if abs(tree.value - target) < abs(closest - target):
            closest = tree.value


        # stop iteration if closest value is equal to target value
        if closest == target:
            break


        # go left if node value is less than target
        if tree.value < target:
            tree = tree.right


        # go right if node value is greater than target
        else:
            tree = tree.left


    # Return closest
    return closest






# This is the class of the input tree. Do not edit.
class BST:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

