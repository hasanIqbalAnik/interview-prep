"""
The idea behind this type of construction is:
1. The first value in the preorder array is the root node.
2. The preorder traversal ensures that all the left children would appear sequentially.
3. Following a similar approach as the previous program, we can construct the tree
by taking values from the preorder array incrementally, finding it in the inorder array, and setting the
 left and right subtree recursively.

 reference link: http://www.geeksforgeeks.org/construct-tree-from-given-inorder-and-preorder-traversal/

 Time Complexity is O(n^2) in the worst case, when the tree is linear.
"""

from node import Node, inorder, preorder


def search(arr, start, end, value):
    for i in range(start, end + 1):
        if arr[i] == value:
            return i


def binary_tree_pre_inorder(iarr, istart, iend, prearr):
    if istart > iend:
        return
    if len(iarr) == 0:
        return

    nd = Node(prearr[binary_tree_pre_inorder.pIndex])
    binary_tree_pre_inorder.pIndex += 1
    if istart == iend:
        return nd

    rdx = search(iarr, istart, iend, nd.val)

    nd.left = binary_tree_pre_inorder(iarr, istart, rdx - 1, prearr)
    nd.right = binary_tree_pre_inorder(iarr, rdx + 1, iend, prearr)

    return nd


prearr = [1, 2, 4, 8, 5, 3, 6, 7]
iarr = [4, 8, 2, 5, 1, 6, 3, 7]
binary_tree_pre_inorder.pIndex = 0

n = binary_tree_pre_inorder(iarr, 0, len(iarr) - 1, prearr)

assert prearr == preorder(n, [])
assert iarr == inorder(n, [])