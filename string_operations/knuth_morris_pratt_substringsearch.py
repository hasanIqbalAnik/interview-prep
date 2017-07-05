def generate_prefix_table(subs):
    """
    Helper function to accompany the KMP. The necessary prefix table is generated here.
    The algorithm is yet to be fully understood. However, the following two links are helpful:

    https://www.youtube.com/watch?v=tWDUjkMv6Lc&
    https://discuss.leetcode.com/topic/21946/detailed-explanation-on-building-up-lps-for-kmp-algorithm
    https://web.stanford.edu/class/cs97si/10-string-algorithms.pdf
    https://discuss.leetcode.com/topic/27261/clean-kmp-solution-with-super-detailed-explanation/2

    :param subs:
    :return:
    """
    pref_table = [0] * len(subs)
    i = 1
    length = 0  # length of the previous longest suffix prefix
    while i < len(subs):
        if subs[i] == subs[length]:
            pref_table[i] = length + 1
            i += 1
            length += 1
        else:
            if length == 0:
                pref_table[i] = 0
                i += 1
            else:
                length = pref_table[length - 1]

    return pref_table


def knuth_morris_pratt(s, pattern):
    """
    Avoiding O(m*n) runtime while searching for substring in a given string.
    Uses O(n) runtime. First a prefix table is built from the substring. It holds the length of the longest prefix
    which is also a suffix in substring. Example: for substring 'abababca':

    char:  | a | b | a | b | a | b | c | a |
    index: | 0 | 1 | 2 | 3 | 4 | 5 | 6 | 7 |
    value: | 0 | 0 | 1 | 2 | 3 | 4 | 0 | 1 |

    Here, at index 0, we only have 'a'. So the no shift is possible. For substring 'ab', the prefix and suffixes are
    'a' and 'b'. The maximum length for matching prefix and suffix is 0. For index 'abab', the prefix and suffixes
    are 'a', 'ab', 'aba' and 'b', 'ab', 'bab'. In this case, the value is 2.

    Now, going over the actual string, every time a mismatch occurs, we look at the prefix table to determine how
    many places we can shift to the right. If pattern 'abab' matches in the string and then a mismatch, then we can
    shift 2 places to the right.

    Time Complexity: O(n), Space Complexity: O(pattern_length)
    reference linK: http://www.keithschwarz.com/interesting/code/knuth-morris-pratt/KnuthMorrisPratt.python.html

    :param s:
    :param subs:
    :return:
    """
    pat_length = len(pattern)
    pref_table = generate_prefix_table(pattern)

    i, q = 0, 0
    
    while i < len(s):
        while q > 0 and s[i] != pattern[q]:
            q = pref_table[q - 1]
        if s[i] == pattern[q]:
            q += 1
        if q == pat_length:
            # return True  # or i - q + 1 for index
            return i - q + 1
        i += 1
    return -1


text = "please help me out so that I could solve this"
pattern = "help"

print knuth_morris_pratt(text, pattern)
