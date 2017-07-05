def reverse_string(s):
    """
    Python doesn't have the facility to reverse a string in place.
    Python strings are immutable. We can use slice operator with negative index.
    But that creates a new string.

    However, in another universe, we could use bitwise XOR operation to do that. 

    :param s:
    :return: reverted string
    """
    return s[::-1]


print reverse_string('asdf')
