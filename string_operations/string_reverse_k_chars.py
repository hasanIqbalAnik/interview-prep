def reverse_in_k_batch(st, k):
    """
    There is a fantastic discussion at this link:
    https://stackoverflow.com/questions/5864271/reverse-a-string-in-python-two-characters-at-a-time-network-byte-order

    The problem is: given a string, we simply don't want to reverse it, we want to do it in batches of k characters.
    For example: if the given string is: 'ABCDEFGH' then taking two characters and reversing them would result in
    'GHEFCDAB'.

    :param st:
    :return:
    """

    # todo generalize it for k, now it works for two characters only

    return "".join(reversed([st[i:i + k] for i in range(0, len(st), k)]))


print reverse_in_k_batch('ABCDEFGH', 3)
