def check_palindrome(str):
    """
    Given a string, it should be determined that whether that string is a palindrome or not.
    :param str:
    :return:
    """
    return str == str[::-1]


print check_palindrome('hasasah')