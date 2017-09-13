class RBTree:

    def __init__(self):
        self.nil = RBTreeNode(0)
        self.root = self.nil

class RBTreeNode:

    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None
        self.parent = None
        self.color = 'black'
