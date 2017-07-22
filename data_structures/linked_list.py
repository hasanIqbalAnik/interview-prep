"""
Linked list is a linear collection of data elements, allowing efficient insertion
and removal from arbitrary element position.

advantages:
-no need to define an initial size
-items can be added or removed from the middle of the list

disadvantages:
-because of the storage of their pointers, they use more memory than arrays
-inherently sequential access
-nodes are stored incontiguously, cpu cache won't work here
-difficult to traverse backwards

applications of linked list:
-stacks and queues can be implemented using linked list
-graphs, hash tables can be implemented using it
"""

"""
task 0: implement a stack using linked list
task 1: reversing a linked list
task 2: delete the middle of a linked list
task 3: detect loop in linked list
task 4: remove loop in linked list
task 5: rotate a linked list
"""


class StackWithLinkedList:
    class _Node:
        def __init__(self, val, next):
            self._val = val
            self._next = next

        def __str__(self):
            return str(self._val)

    def __init__(self):
        self._head = None
        self._size = 0

    def push(self, val):
        self._head = self._Node(val, self._head)
        self._size += 1

    def pop(self):
        if not self.is_empty():
            item = self._head._val
            self._head = self._head._next
            self._size -= 1
            return item
        else:
            raise Exception('Stack is empty')

    def peek(self):
        if self.is_empty():
            raise Exception('asdf')
        return self._head._val

    def is_empty(self):
        return self._size == 0


if __name__ == '__main__':
    linked_stack = StackWithLinkedList()
    map(linked_stack.push, [x for x in xrange(5)])
    print linked_stack.pop()
