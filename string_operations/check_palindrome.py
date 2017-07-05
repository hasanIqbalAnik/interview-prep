def check_palindrome(str):
    """
    Given a string, it should be determined that whether that string is a palindrome or not.
    :param str:
    :return:
    """
    return str == str[::-1]


def check_palin(word):
    """
    Code taken from https://stackoverflow.com/questions/29446433/reversing-a-string-and-palindrom-time-complexity-in-python
    A little more efficient. But the time complexity is still O(n)

    :param word:
    :return:
    """
    for i in xrange(len(word) / 2):
        if word[i] != word[-(i + 1)]:
            return False
    return True


print check_palindrome('hasasah')
print check_palin('hasasah')
