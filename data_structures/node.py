class Node:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

    def __str__(self):
        return str(self.val)


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


def preorder(root, result):
    if root:
        result.append(root.val)
        preorder(root.left, result)
        preorder(root.right, result)
    return result
