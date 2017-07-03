def lis_dp(array):
    """
    find out the longest increasing subsequence using the following algorithm:

    initialize an array LIS with 1s to hold the increasing subsequence lengths at each of the array positions.
    use two pointers i and j. i goes from 0 to len(array)-1. j goes from 0 to i.
    in each of these cases, check whether the value at array[j] is less than array[i]. if it is, then we have found a
    partial increasing subsequence. check whether the LIS value stored in the position J and add one with it is greater than the value
    stored in the LIS position i. Else, we have to increase the value of index i and proceed to the next iteration.

    time complexity: O(n^2), space complexity O(n).

    :param array: an array where we are interested to find out the lis
    :return: length of the longest increasing subsequence
    """

    lis = [1] * len(array)
    i = 1

    while i < len(array):
        j = 0
        while j < i:
            if array[i] > array[j] and lis[j] + 1 > lis[i]: # we've identified an increasing subsequence
                lis[i] = lis[j] + 1
            j += 1
        i += 1

    return max(lis)



def lis_recursive(array):
    """
    find out the longest increasing subsequence using recursive calling

    :param array:
    :return: length of the lis
    """

    #TODO
    



a = [3, 2, 1, 4, 8, 7, 5, 9, 10, 4]
print lis_dp(a)
# output is 5. (3, 4, 7, 9, 10)
