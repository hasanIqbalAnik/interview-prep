def lcs_dp(s1, s2):
    """
    find out the longest common subsequence of two given strings, or iterables, in that case the code
    should be changed a little.

    time complexity of the native implementation is O(2^n). The DP approach using memoization is O(m*n)

    example: s1 = AGTAB, s2 = GXTXAYB, then lcs(s1, s2) = 'GTAB'

    :param s1: the first string
    :param s1: the first string

    :return length of the longest common subsequence
    """

    T = [[0 for j in range(len(s2) + 1)] for i in range(len(s1) + 1)]
    i = 1
    resultarr = []
    while i <= len(s1):
        j = 1
        while j <= len(s2):
            if s1[i - 1] == s2[j - 1]:
                T[i][j] = T[i - 1][j - 1] + 1
            else:
                T[i][j] = max(T[i - 1][j], T[i][j - 1])
            j += 1
        i += 1
    # at this point, the resulting matrix has been generated. the last cell would hold the length
    # to regenerate the actual substring, let's do some more calculation

    x, y = len(s1), len(s2)
    while x != 0 and y != 0:
        if T[x][y] == T[x-1][y]:    # result came from previous row, same column
            x -= 1
        elif T[x][y] == T[x][y-1]:  # result came from previous column, same row
            y -= 1
        else:                       # there was a match, append this character to the result
            resultarr.append(s1[x-1])
            x -= 1
            y -= 1

    return ''.join(resultarr[::-1]), T[-1][-1]  # should be printed in the reversed order


def lcs_recursive(xstr, ystr):
    """
    recursive way to find out the longest common subsequence. time complexity: O(2^n)
    :param xstr: first string
    :param ystr: second string
    :return: the longest common subsequence
    """

    if not xstr or not ystr:
        return ""
    x, xs, y, ys = xstr[0], xstr[1:], ystr[0], ystr[1:]
    if x == y:
        return x + lcs_recursive(xs, ys)
    else:
        return max(lcs_recursive(xstr, ys), lcs_recursive(xs, ystr), key=len)

print lcs_recursive('AGTAB', 'GXTXAYB')
print lcs_dp('AGTAB', 'GXTXAYB')
