def merge(a1, a2):
    """
    merge two sorted arrays

    example: a1 = [2, 4, 6], a2 = [1, 3, 5] then result = [1, 2, 3, 4, 5]

    :param a1: sorted array 1
    :param a2: sorted array 2

    :return result: merged array of the inputs
    """

    i, j = 0, 0
    result = []  # resulting array
    while i < len(a1) and j < len(a2):  # both array have iterables
        if a1[i] < a2[j]:
            result.append(a1[i])
            i += 1
        elif a1[i] > a2[j]:
            result.append(a2[j])
            j += 1
        else:
            result.append(a1[i])
            result.append(a2[j])
            i += 1
            j += 1

    if i == len(a1):  # array a1 was exhaused, append the remaining contents of the second array to the result
        result.extend(a2[j:])
    if j == len(a2):  # array a2 was exhaused, append the remaining contents of the first array to the result
        result.extend(a1[i:])

    return result


def mergesort(array):
    """
    Repeatedly split and sort the parts and finally combine the results to get
    a sorted array.

    :param array: the input array
    :return array: the sorted output
    """
    if len(array) == 1:
        return array
    mid = len(array) // 2  # find the middle point of the array
    left = mergesort(array[:mid])
    right = mergesort(array[mid:])
    return merge(left, right)


print mergesort([3, 5, 1, 100, 500, 3, 4, 5, 6, 9, 2, 9])
