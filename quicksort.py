def quicksort_xtra_mem(alist):
    if alist:
        pivot = alist[0]
        below = [x for x in alist[1:] if x < pivot]
        above = [x for x in alist[1:] if x >= pivot]

        return quicksort_xtra_mem(below) + [pivot] + quicksort_xtra_mem(above)
    else:
        return alist


def partition(array, begin, end):
    pivot = begin
    for i in xrange(begin + 1, end + 1):
        if array[i] <= array[begin]:
            pivot += 1
            array[i], array[pivot] = array[pivot], array[i]
    array[pivot], array[begin] = array[begin], array[pivot]
    return pivot


def quicksort(array, begin, end):
    if begin < end:
        pivot = partition(array, begin, end)
        quicksort(array, begin, pivot - 1)
        quicksort(array, pivot + 1, end)


array = [3, 4, 1, 2, 5, 10, 12, 5, 2, 1, 5, 3, 100]
print quicksort_xtra_mem(array)
quicksort(array, 0, len(array) - 1)
print array
