"""
1. Construct a binary search tree from sorted array
2. Searching
3. Insertion
4. Deletion
"""

from node import Node, preorder, inorder, postorder


def construct_bst_from_sorted_array(arr, l, r):
    """
    Following a simple binary search procedure yields a binary search tree.
    Time Complexity: O(n)
    Space complexity: O(logn)
    :param arr:
    :param l:
    :param r:
    :return:
    """
    if l > r:
        return
    mid = l + (r - l) // 2
    root = Node(arr[mid])

    root.left = construct_bst_from_sorted_array(arr, l, mid - 1)
    root.right = construct_bst_from_sorted_array(arr, mid + 1, r)

    return root


def search_in_bst(root, val):
    """
    O(logn) or O(h) search in bst, represented by the root node. here h represents the height of the tree
    :param root: root index of the bst
    :param val: the value to look for
    :return: Node if found, None otherwise
    """

    if root is None or root.val == val:
        return root
    if root.val < val:
        return search_in_bst(root.right, val)
    return search_in_bst(root.left, val)


def insert_in_bst(root, val):
    """
    Inserting a new node built from the value is to be inserted in the bst.
    Time complexity: same as search. O(h), but in the worst case, h could be equal to n
    :param root:
    :param val:
    :return:
    """
    if not root:
        return Node(val)
    if root.val > val:
        root.left = insert_in_bst(root.left, val)
    else:
        root.right = insert_in_bst(root.right, val)

    return root


def deletion_in_bst(n, val, parent=None):
    """
    Compared to the other two methods, deletion is a little trickier. There are three scenarios
    while deleting a node in bst:
    1. The node is a leaf
    2. It has one child
    3. It has two children

    The first case is pretty straightforward to handle. We can simply remove it.

    If it has only one child, then this child should be set as the left or right child of it's parent.

    If it has two children, then the minimum element of it's right subtree or the maximum
    element of it's left subtree should be copied in it's place. Then duplicated should be removed.


    :param n:
    :param val:
    :return:
    """

    if not n or val is None:
        return None
    if n.val > val:  # then delete on the left subtree
        n.left = deletion_in_bst(n.left, val)
    elif n.val < val:  # then delete on the right subtree
        n.right = deletion_in_bst(n.right, val)
    else:  # found the node to delete
        if not n.left and not n.right:  # if it doesn't have ny child, simply return None to it's parent
            return None
        if not n.left:  # but has a right child
            right = n.right
            del n
            return right
        elif not n.right:  # has a left child but not a right
            left = n.left
            del n
            return left
        else:  # hardest case, where node has two children
            min_node = n.right
            while min_node.left:  # find the minimum on the right
                min_node = min_node.left
            n.val = min_node.val  # set the minimum value to the root to be deleted
            n.right = deletion_in_bst(n.right, min_node.val)  # remove the duplicate value on the right subtree
    return n  # return the root


def find_min_val_in_bst(root):
    if not root:
        return float('inf')
    return min(root.val, find_min_val_in_bst(root.left), find_min_val_in_bst(root.right))


a = [1, 2, 3, 4, 5, 6, 7, 8]
r = construct_bst_from_sorted_array(a, 0, len(a) - 1)
deletion_in_bst(r, 2)
print preorder(r, [])
