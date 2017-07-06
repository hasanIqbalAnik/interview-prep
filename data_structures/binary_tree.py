"""
The idea of reconstructing a binary tree from the post and inorder traversal works like the following:
1. We know that the last element of the post order traversal is the root.
2. Take this node and find it's position in the inorder array.
3. The left half of the root index in the inorder array is the left subtree.
4. Similarly the right half of the root index in the inorder array is the right subtree.
5. Use recursion on these right and left subtree and assign them to the root.


"""


# todo replace global variable pIndex with some sort of a parameter

class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None


def binary_tree_in_post(inarr, instart, inend, postarr):
    global pIndex
    if instart > inend:
        return
    if len(inarr) == 0:
        return
    nd = Node(postarr[pIndex])
    pIndex -= 1
    if instart == inend:
        return nd
    index = instart  # to look for the index of the root in the inorder array
    while index < inend:
        if inarr[index] == nd.val:
            break
        index += 1
    nd.right = binary_tree_in_post(inarr, index + 1, inend, postarr)
    nd.left = binary_tree_in_post(inarr, instart, index - 1, postarr)

    return nd


def inorder(root, result):
    if root:
        inorder(root.left, result)
        result.append(root.val)
        inorder(root.right, result)
    return result


def postorder(root, result):
    if root:
        postorder(root.left, result)
        postorder(root.right, result)
        result.append(root.val)
    return result


parr = [8, 4, 5, 2, 6, 7, 3, 1]
iarr = [4, 8, 2, 5, 1, 6, 3, 7]
pIndex = len(parr) - 1

n = binary_tree_in_post(iarr, 0, len(iarr) - 1, parr)
assert parr == postorder(n, [])
assert iarr == inorder(n, [])
