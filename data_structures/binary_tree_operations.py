"""
This file contains the usual operations performed in a binary tree. Namely, search, insert and delete a node from it .
"""

from node import Node, preorder, inorder


def search(n, val):
    if n:
        if n.val == val:
            return n
        return search(n.left, val) or search(n.right, val)

def insert(n, val):
    """
    run a bfs on root. the first null child should be replaced with the new node.
    :param val:
    :return:
    """
    # todo insertion not fully understood
    if n:
        if not n.left:
            n.left = Node(val)
            return
        elif not n.right:
            n.right = Node(val)
            return
        return insert(n.left, val)
        return insert(n.right, val)



def delete(n, val):
    """
    run a dfs and match nodes value with the given val. If found, set it's parent's this child to null.
    :param n:
    :param val:
    :return:
    """

    if n:
        if n.val == val:
            print 'here'
            n = None
            return
        elif n.left:
            if n.left.val == val:
                n.left = None
        elif n.right:
            if n.right.val == val:
                n.right = None
        else:
            delete(n.left, val)
            delete(n.right, val)

n1, n2, n3, n4, n5, n6, n7, n8 = Node(1), Node(2), Node(3), Node(4), Node(5), Node(6), Node(7), Node(8)
n1.left, n1.right, n2.left, n2.right, n3.left, n3.right, n4.left = n2, n3, n4, n5, n6, n7, n8


print preorder(n1, [])
delete(n1, 4)
print preorder(n1, [])