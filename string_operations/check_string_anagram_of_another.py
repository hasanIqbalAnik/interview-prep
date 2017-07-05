"""
Two ways to see if a string is an anagram of another string is given below.
The first one sorts both string and sees if they are equal.

Time complexity for sorting is O(nlogn) and for checking string equality it's O(n). So in total it's O(nlogn).

The second method beings by creating hashtable of all the possible characters. For the first string
all the occurrences of the characters in the hashtable is incremented by 1. Then for the
second string, these occurrences are decremented. If the final hashtable has any non zero value,
then they are not anagram of each other.

The time complexity is O(n). However the space complexity depends on the type of characterset being used.
If only english alphabet is used, then its constant to 26.

Useful snippet:
    # l = [chr(x) for x in xrange(ord('A'), ord('Z') + 1)]
    # l.extend([chr(x) for x in xrange(ord('A'), ord('Z') + 1)])
    #
    # d = {chr(x): 0 for x in xrange(ord('a'), ord('z') + 1)}
    # d.update({chr(x): 0 for x in xrange(ord('A'), ord('Z') + 1)})


"""


def check_anagram_sorting(s1, s2):
    """
    :param s1:
    :param s2:
    :return:
    """
    return sorted(s1) == sorted(s2)


def check_anagram_hashtable(s1, s2):
    """
    :param s1:
    :param s2:
    :return: Whether the two strings are anagrams of each other or not
    """
    d = {chr(x): 0 for x in xrange(ord('a'), ord('z') + 1)}
    d.update({chr(x): 0 for x in xrange(ord('A'), ord('Z') + 1)})

    for c in s1:
        d[c] = d[c] + 1

    for c in s2:
        d[c] = d[c] - 1

    if sum(d.values()) != 0:
        return False
    else:
        return True



print check_anagram_sorting('silent', 'listen')
print check_anagram_hashtable('silent', 'listen')