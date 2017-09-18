def partition(array, begin, end):
    """
    Partition method to return an appropriate pivot to be used to split the array

    :param array: the array to be sorted
    :param begin: starting point
    :param end: ending point
    :type begin: integer
    :type end: integer
    :return: the pivot, this is the appropriate index
    :rtype: integer
    """
    pivot = begin
    for i in xrange(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort_xtra_mem(alist):
    """
    Sort an array of integers using quicksort algorithm

    :param alist: a list of integers
    :type alist: list
    :return: sorted array
    :rtype: list
    """
    if alist:
        pivot = alist[0]
        below = [x for x in alist[1:] if x < pivot]
        above = [x for x in alist[1:] if x >= pivot]

        return quicksort_xtra_mem(below) + [pivot] + quicksort_xtra_mem(above)
    else:
        return alist


def quicksort(array, begin, end):
    """
    Implementation of quicksort. Needs the help of a partition function.

    :param array: A list of integers
    :param begin: Starting point
    :param end: Ending point
    :return: Sorted rray
    """
    if begin < end:
        pivot = partition(array, begin, end)
        quicksort(array, begin, pivot - 1)
        quicksort(array, pivot + 1, end)


array = [3, 4, 1, 2, 5, 10, 12, 5, 2, 1, 5, 3, 100]
print array
print quicksort_xtra_mem(array)
quicksort(array, 0, len(array) - 1)
print array
