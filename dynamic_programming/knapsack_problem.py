def knapsack_problem_dp(weights, values, capacity):
    """
    The dynamic programming approach to solve this problem is based on the similar philosophy.
    All we are doing here is storing the partial solutions and reusing it.

    Time complexity: O(m*n), Space Complexity O(m*n)

    :param weights: array of weights of the items.
    :param values: array of respective values
    :param capacity: current capacity of the knapsack
    :return: maximum value obtainable from these items, weights and size of knapsack
    """
    dp = [[0 for x in xrange(capacity + 1)] for y in xrange(len(weights) + 1)]

    for i in xrange(1, len(weights) + 1):
        for j in xrange(1, capacity + 1):
            if weights[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                dp[i][j] = max(dp[i - 1][j], values[i - 1] + dp[i - 1][j - weights[i - 1]])

    return dp[-1][-1]


def knapsack_problem_recursive(weights, values, capacity, n):
    """
    The base cases are signifying whether the capacity has become 0 or if the index has gone less than 0.
     we have to return 0 in both cases.
     In other cases, if the weight of the current item is larger than the capacity, then we definitely can't
     take this item. So the solution would be to return the result of other items.

     However, if we do have the capacity to take it, there comes the question whether we should take it or not.
     We should take the maximum of either of these cases.

    Time Complexity of this solution is: O(2^n)

    :param weights: array of weights of the items.
    :param values: array of respective values
    :param capacity: current capacity of the knapsack
    :param n: index of the last item in the array
    :return: maximum value obtainable from these items, weights and size of knapsack
    """
    if capacity == 0 or n < 0:
        return 0
    if weights[n] > capacity:
        return knapsack_problem_recursive(weights, values, capacity, n-1)
    else:
        return max(values[n] + knapsack_problem_recursive(weights, values, capacity - weights[n], n-1), knapsack_problem_recursive(weights, values, capacity, n-1))

# weights = [1, 2, 4, 2, 5]
# values = [5, 3, 5, 3, 2]
# capacity = 10

w = [2, 3, 4, 5]
v = [3, 4, 5, 6]
c = 5

print knapsack_problem_dp(w, v, c)
print knapsack_problem_recursive(w, v, c, len(w) - 1)
