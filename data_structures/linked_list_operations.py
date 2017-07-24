"""
Several common linked list operations like creating, traversing, deleting, reversing
for a singly linked list is presented here.

task 1: reversing a linked list
task 2: delete the middle of a linked list
task 3: detect loop in linked list
task 4: remove loop in linked list
task 5: rotate a linked list

"""


class Node:
    def __init__(self, elem, next_node):
        self._elem = elem
        self._next = next_node

    def __str__(self):
        return str(self._elem)


# noinspection PyProtectedMember,PyCompatibility
class LinkedList:
    def __init__(self):
        self._head = None
        # could use a size variable, but that omits some algorithmic complexity for measuring the size

    def insert(self, elem):
        """creating an element and adding into the linked list head"""
        self._head = Node(elem, self._head)

    def delete_first(self, elem):
        """delete the occurrences of elements at the head or right after head positions"""
        if not self._head:
            raise Exception('unable to delete form an empty list')

        while self._head:
            if self._head._elem == elem:
                self._head = self._head._next
            else:
                break

    def delete_all(self, elem):
        """delete all occurrence of given element"""

        self.delete_first(elem)  # delete any occurrence at the head

        current, prev = self._head, self._head
        while current:
            if current._elem == elem:
                prev._next = current._next
                current = prev._next
            else:
                prev = current
                current = current._next

    def reverse_nodes(self):
        """reverse the whole list."""
        current = self._head
        prev = None
        while current:
            temp = current._next
            current._next = prev
            prev = current
            current = temp
        self._head = prev  # restore the head

    def detect_loop(self):
        """check whether any circular reference exists in any part of the chain.
        the fast pointer is advanced two nodes at a time. if at any point these two pointers meet, then
        there is a loop. we can keep track of the previous node of the slow pointer to remove
        the loop by setting it's next to none. """
        slow_pointer, fast_pointer = self._head, self._head
        slow_prev = slow_pointer
        while slow_pointer and fast_pointer and fast_pointer._next:  # if there isn't a loop, fast pointer would be None
            slow_prev = slow_pointer
            slow_pointer = slow_pointer._next
            fast_pointer = fast_pointer._next._next
            if slow_pointer == fast_pointer:
                return slow_prev
        return False

    def remove_loop(self):
        loop_node = self.detect_loop()
        if loop_node:
            loop_node._next = None

    def rotate_list(self, k):
        if not self._head or not self._head._next or k == 0:
            return self._head

        current, count = self._head, 1
        while current._next:  # measure the length of the total list
            count += 1
            current = current._next
        current._next = self._head  # establish the circular relation, tail is now pointing to head
        k = k % count  # k can be very big, it must not exceed the length of the chain
        for i in xrange(count - k):
            current = current._next  # place the current pointer to just before the new head
        self._head = current._next  # replace the head with the current's next value
        current._next = None  # set the current's next value to null, thus breaking the loop

    def delete_middle(self):
        """if there are n nodes in the list, delete the n/2 th node. if n is even, delete the second of the
        two middle nodes. the obvious solution is to traverse the list and measuring the size.
        this requires n + n/2 number of loop execution. however, this can be done in
        n/2 iteration only. the idea is to use two pointers. one slow and one fast.
        if the fast pointer is advanced two nodes each time, by the time it reaches the
        end, the slow pointer would be at the middle element. """

        slow_pointer, fast_pointer, slow_prev = self._head, self._head, None
        while fast_pointer and fast_pointer._next:
            fast_pointer = fast_pointer._next._next
            slow_prev = slow_pointer
            slow_pointer = slow_pointer._next

        slow_prev._next = slow_pointer._next


    def print_nodes(self):
        """temp is used to make sure head remains at the first position after the traversal"""
        temp = self._head
        while temp:
            print temp._elem,
            temp = temp._next
        print


if __name__ == '__main__':
    ll = LinkedList()

    nd1 = Node(1, None)
    nd2 = Node(2, None)
    nd3 = Node(3, None)
    nd4 = Node(4, None)
    nd5 = Node(5, None)
    nd6 = Node(6, None)
    nd1._next = nd2
    nd2._next = nd3
    nd3._next = nd4
    nd4._next = nd5
    nd5._next = nd6

    ll._head = nd1
    ll.print_nodes()
    ll.delete_middle()
    ll.print_nodes()
