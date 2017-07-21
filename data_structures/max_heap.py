"""
Building a max heap is the same process as building a binary search tree
with an additional property that ensures that always the maximum element is
at the root.
*Heap is a complete binary tree.
*heaps are implemented using arrays, unlike other tree data structure
*heapsort complexity is O(n * logn)
*guarantees O(log n) performance in insertion, deletion.
*guarantees O(1) performance extract max


algorithm for the construction of a maxheap:
1. for each of the array elements, insert into the heap
2. inserting means adding an element at the end of the array.
3. after addition, check whether the new element is greater than it's parent.
4. if so, swap them.
5. continue this process until either the element has no parent, or it's not greater than it's parent

this is essentially the heapify up method.

algorithm for deletion in a heap:
1. execute extract min, this should be the first element of the array.
2. copy the last element of the array to the first element.
3. check whether the first element now is less than either of the children.
4. if so, swap with the left or right children, whichever is greater.
5. continue this process all the way down the tree untile the max heap property is restored.

this is essentially the heapify down method.

there are some other helper methods which can also be declared as statics, like get parent,
get children or their indices.

reference link: https://www.youtube.com/watch?v=t0Cq6tVNRBA
"""


class MaxHeap:
    def __init__(self, items=None):
        self.items = []
        self.size = 0
        if items:
            self.build_heap(items)

    def build_heap(self, items):
        for item in items:
            self.insert(item)

    def get_left_child_index(self, index):
        return 2 * index + 1

    def get_right_child_index(self, index):
        return 2 * index + 2

    def get_parent_index(self, index):
        return (index - 1) // 2

    def has_left_child(self, index):
        return self.get_left_child_index(
            index) < self.size  # array index always starts from 0, so last index is size - 1

    def has_right_child(self, index):
        return self.get_right_child_index(index) < self.size

    def has_parent(self, index):
        return self.get_parent_index(index) >= 0

    def left_child(self, index):
        return self.items[self.get_left_child_index(index)]

    def right_child(self, index):
        return self.items[self.get_right_child_index(index)]

    def parent(self, index):
        return self.items[self.get_parent_index(index)]

    def insert(self, item):
        self.items.append(item)
        self.size += 1
        self.heapify_up()

    def extract_max(self):
        if self.size == 0:
            raise IndexError
        item = self.items[0]
        self.items[0] = self.items[self.size - 1]
        self.size -= 1
        self.heapify_down()
        del self.items[len(self.items) - 1]
        return item

    def heapify_up(self):
        """
        used to re-establish heap property after an item is inserted at the end
        :return:
        """
        index = self.size - 1
        while self.has_parent(index) and self.parent(index) < self.items[index]:
            self.items[index], self.items[self.get_parent_index(index)] = self.items[self.get_parent_index(index)], \
                                                                          self.items[index]
            index = self.get_parent_index(index)

    def heapify_down(self):
        """
        used to re-establish heap property after extract min
        :return:
        """
        index = 0
        while self.has_left_child(index):
            larger_idx = self.get_left_child_index(index)
            if self.has_right_child(index) and self.right_child(index) > self.left_child(index):
                larger_idx = self.get_right_child_index(index)
            if self.items[larger_idx] > self.items[index]:
                self.items[index], self.items[larger_idx] = self.items[larger_idx], self.items[index]

            else:
                break
            index = larger_idx


if __name__ == '__main__':
    arr = [10, 15, 20, 17, 25]
    hp = MaxHeap(arr)
    while True:
        try:
            print hp.extract_max(),  # should print the array in sorted order
        except IndexError:
            break
