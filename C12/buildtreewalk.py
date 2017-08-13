class Node(object):

    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right

def build_tree(x, root):
    if x.val <= root.val:
        if not root.left:
            root.left = x
        else:
            build_tree(x, root.left)
    else:
        if not root.right:
            root.right = x
        else:
            build_tree(x, root.right)

def inorder_tree_walk(node):
    if node:
        inorder_tree_walk(node.left)
        print node.val
        inorder_tree_walk(node.right)


t3 = Node(3, None, None)
t1 = Node(1, None, None)
t8 = Node(8, None, None)
t2 = Node(2, None, None)
t6 = Node(6, None, None)
t7 = Node(7, None, None)
t5 = Node(5, None, None)

ll = [t1, t8, t2, t6, t7, t5]

for x in ll:
    build_tree(x, t3)

inorder_tree_walk(t3)