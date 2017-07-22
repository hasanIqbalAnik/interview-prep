"""
Stack is a simple data structure, allowing only push, pop or maybe peek operations.
It's used in a lot of applications like:

-expression evaluation
-to reverse a word
-undo mechanisms in text editors
-back/forward buttons in browsers
-recursions
-memory management in the OS

It can be implemented using arrays or linked lists. The advantage of using one over the other
would be evident depending on the data and the algorithm. A linked list with a tail pointer
would guarantee O(1) worst case performance while an array would provide the same in
amortized analysis. Also, linked list does entail a little memory overhead for saving
the extra piece of memory for the pointers.

"""


class Stack:
    """
    An array based implementation of the stack data structure.
    """

    def __init__(self):
        self.stack = []

    def push(self, element):
        self.stack.append(element)

    def pop(self):
        if self.is_empty():
            raise IndexError
        item = self.stack[len(self.stack) - 1]
        del self.stack[len(self.stack) - 1]
        return item  # returning the last element, O(1)

    def peek(self):
        if self.is_empty():
            raise IndexError
        return self.stack[len(self.stack) - 1]  # returning the last element, O(1)

    def is_empty(self):
        if not len(self.stack):
            True
        return False


if __name__ == '__main__':
    st = Stack()
    a = [x+1 for x in xrange(3)]
    map(st.push, a)
    print st.pop()
    print st.pop()

    st.push(100)
    print st.peek()