def maximum_subarray(array):
    """
    Kadane's algorithm with modification to find out the maximum subarray problem.
    The alogorithm works like this: if there is only one element in the array,
    then the best sum possible is that element itself. When there are two
    elements in the array, the local maximum is the sum of the first element +
    the recent element or the recent element itself. the global maximum
    should only be updated when the local maximum is more than that. The indices
    are defined to store the first and last position of the maximum array.
    Without the modifications, Kadane's algorithm is just two lines:

    max_ending_here = max(item + max_ending_here, item)
    max_so_far = max(max_so_far, max_ending_here)

    The time complexity of this algorithm is O(n),
    The space complexity is(without the recursion): O(1)

    :param array: input array
    :return: the maximum sum, starting index of that max_sum and the end of point of that sum
    """
    local_start, local_end, mx_start, mx_end = 0, 0, 0, 0
    max_ending_here = max_so_far = array[0]
    i = 1
    while i < len(array):
        if array[i] + max_ending_here > array[i]:
            local_end = i
            max_ending_here = array[i] + max_ending_here
        else:
            max_ending_here = array[i]
            local_start = i

        if max_ending_here > max_so_far:
            mx_start = local_start
            mx_end = local_end
            max_so_far = max_ending_here
        i += 1

    return max_so_far, mx_start, mx_end


a = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print maximum_subarray(a)
# output 4, -1, 2, 1 -> 6
