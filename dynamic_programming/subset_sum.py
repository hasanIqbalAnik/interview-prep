def subset_sum_dp(elements, target):
    """
    Given an array and a target, the goal is to find out whether the target sum could be obtained by
    any combination of the array elements. However, the brute force approach takes O(2^n) time. This dp
    approach takes O(mn) time with O(mn) space complexity. It can't work on negative numbers.

    :param elements: array of numbers
    :param target: the number to find
    :return: True if, target can be obtained, else False
    """
    T = [[False for x in range(target + 1)] for y in range(len(elements) + 1)]

    for i in xrange(target + 1):  # if there are no elements, no target can be satisfied
        T[0][i] = False

    for i in xrange(len(elements) + 1):  # if the target is 0, then any set will make it True
        T[i][0] = True

    for i in xrange(1, len(elements) + 1):
        for j in xrange(1, target + 1):
            if j - elements[
                        i - 1] < 0:  # the element is larger than the current target, put the value immediately above
                T[i][j] = T[i - 1][j]
            else:
                T[i][j] = T[i - 1][j] or T[i - 1][
                    j - elements[i - 1]]  # the element is smaller than the target, subtract the elem and
                # check whether the remaining target could be achieved without this element

    return T[-1][-1]


def subset_sum_recursive(array, target, n):
    """
    Recursive approach to find the same thing as mentioned before. This approach too, is exponential in runtime.

    :param array:
    :param target:
    :param n:
    :return:
    """
    # base cases
    if target == 0:
        return True
    if len(array) == 0 and target != 0:
        return False
    if n < 0:
        return False
    return subset_sum_recursive(array, target-array[n], n-1) or subset_sum_recursive(array, target, n-1)


# a = [1, 3, 9, 2]
a = [3, 4, 5, 2, 5, 5, 29, 100]


print subset_sum_dp(a, 34)
# print subset_sum_recursive(a, 8, len(a)-1)