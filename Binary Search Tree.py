__author__ = 'Xing'

#原理懂，但是class看不太懂！

class Node:
    lft = None
    rgt = None
    def __init__(self, key, val):
        self.key = key
        self.val = val

def insert(node, key, val):
    if node is None: return Node(key, val) # Empty leaf: add node here
    if node.key == key: node.val = val     # Found key: replace val
    elif key < node.key:                   # Less than the key?
        node.lft = insert(node.lft, key, val)  # Go left
    else:
        node.rgt = insert(node.rgt, key, val)  # Go right
    return node


def search(node, key):
    if node is None:  # Empty leaf: it's not here
        raise KeyError
    if node.key == key: # Found key: return val
        return node.val
    elif key < node.key:  # Less than the key?
        return search(node.lft, key)  # Go left
    else:
        return search(node.rgt, key)  # Go right

class Tree:   #simple wrapper
    root = None
    def __setitem__(self, key, val):
        self.root = insert(self.root, key, val)
    def __getitem__(self, key):
        return search(self.root, key)
    def __contains__(self, key):
        try: search(self.root, key)
        except KeyError: return False
        return True
