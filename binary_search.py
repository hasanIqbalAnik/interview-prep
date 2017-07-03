def binary_search_recursive(array, start, end, elem):
    """
	Recursive approach for binary search. Uses O(k) extra memory for the stack frames. O(1) for the best case 
	runtime and O(logn) in the worst case.
	
	:param array: the sorted array to search in
	:param start: starting point of the array
	:param end: ending point of the array
	:param elem: the element to look for
	:retrun index: the actual index of the element in the array, or -1 if not found
	"""

    if start > end:
        return -1
    if array:
        mid = start + (end - start) // 2
        if array[mid] == elem:
            return mid
        elif array[mid] < elem:
            start = mid + 1
            return binary_search_recursive(array, start, end, elem)
        else:
            end = mid - 1
            return binary_search_recursive(array, start, end, elem)


def binary_search_iterative(array, elem):
    """
	Iterative approach for binary search. O(1) extra memory. Runtime is O(logn)
	
	:param array: the sorted array to search in
	:param elem: the element to look for
	:retrun index: the actual index of the element in the array, or -1 if not found
	"""
    start = 0
    end = len(array) - 1

    while start <= end:
        mid = start + (end - start) // 2
        if array[mid] == elem:
            return mid
        elif array[mid] < elem:
            start = mid + 1
        else:
            end = mid - 1
    return -1


a = [1, 2, 3, 4, 5, 6, 7, 8]
# print binary_search_recursive([], 0, len(a) - 1, 8)
# print binary_search_iterative(a, 5)
