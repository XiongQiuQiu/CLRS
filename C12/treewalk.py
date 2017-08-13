class Node(object):

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right  = right

def inorder_tree_walk(node):

    if node:
        inorder_tree_walk(node.left)
        print node.val
        inorder_tree_walk(node.right)

def preorder_tree_walk(node):
    if node:
        print node.val
        preorder_tree_walk(node.left)
        preorder_tree_walk(node.right)

def postorder_tree_walk(node):
    if node:
        postorder_tree_walk(node.left)
        postorder_tree_walk(node.right)
        print node.val

t2 = Node(2, None, None)
t5 = Node(5, None, None)
t5_ = Node(5, t2, t5)
t8 = Node(8, None, None)
t7 = Node(7, None, t8)
t6 = Node(6, t5_, t7)

print 'inorder_tree_walk'
inorder_tree_walk(t6)
print 'preorder_tree_walk'
preorder_tree_walk(t6)
print 'postorder_tree_walk'
postorder_tree_walk(t6)