"""
Bit Manipulations(AND, OR, NOT, XOR and so on) are used in a lot of ways. It's efficient, fast and requires very little memory.
Applications include:
1. Encryption
2. Calculating checksums
3. Anywhere boolean flags are needed to represent something
4. Compression algorithms
5. Graphics manipulation

We can measure the memory footprint of these bitarray objects using the command:
Two modules that python offers named bitstring and bitarray both lets to work
with bits. However, bitstring seems to consume less memory for basic operaitons.
For example in the following snippet:

from bitstring import BitArray
from bitarray import bitarray
import sys

a, b = BitArray(0), bitarray(0)
print 'size of a', sys.getsizeof(a), ' ', 'sizeof b: ', sys.getsizeof(b)
# outputs 56, 112 as their respective size

In these manipulation tasks, we will be using BitArray. These operations in decimal format
is a hell lot easier to understand and perform. It's just about practicing with BitArray.

for example:

check ith bit: 5 & (1 << 3)  => produces 0
turn ith bit on: 5 | (1 << 3)
and so on. 


Reference: Programming Contest: Data Structure and Algorithms by Md. Mahbubul Hasan
"""

from bitstring import BitArray


def create_and_shift_ones(bit_string, i):
    """create bit array of value 1 and then shift it to the left i times. """

    str_length = len(bit_string)
    if i > (str_length - 2):  # deducting 2 for the '0b' of every binary string
        raise Exception('Shifting more than the length of the string')
    one = BitArray('0b' + '0' * (str_length - 1) + bin(1)[2:])  # create a bitarray of ones of that length
    return one.__ilshift__(i)  # shift the binary representation of 1, i times.


def check_ith_bit_off(bit_string, i):
    """
    after creating a bitstring of ones with the equal lenght of the
    given string, if this output is 1, then that ith bit is 1, else not.
    (x & (1 << i))
    Example:
        110110 -> 54 in decimal. the bit count starts from the left.
        0th bit is 0
        1st bit is 1
        2nd bit is 1
        3rd bit is 0
        and so on...

        now to check whether the 0th bit is 0 or not, we left shift the value 1, 0 times, which is itself.
        then we perform and operation with that number:
        110110
        000001
      -----------
        000000
        this means, the 0th bit is set to 0 in this case.

        For the 1st bit, which is 1, we can check accordingly, shifting 1, one time.
        110110
        000010
      ----------
        000010
        so this value is non-zero. means the 1st bit is 1.

    """
    one = create_and_shift_ones(bit_string, i)
    return bit_string.__and__(one).int == 0  # AND those two numbers and check whether it produces 0 or not


def turn_ith_bit_on(bit_string, i):
    """almost same as the bit on/off checking, only using OR, instead of AND: (x | (1 << i))"""
    one = create_and_shift_ones(bit_string, i)
    return bit_string.__or__(one)


def toggle_ith_bit(bit_string, i):
    """Using XOR will toggle the ith bit: (x ^ (1 << i))"""
    one = create_and_shift_ones(bit_string, i)
    return bit_string.__xor__(one)


def turn_ith_bit_off(bit_string, i):
    """If the ith bit is on, then set it to off. else do nothing"""
    if not check_ith_bit_off(bit_string, i):  # if true, then the ith bit is not 0, we have to set it off
        return toggle_ith_bit(bit_string, i)
    else:
        return bit_string


def set_all_off_except_last_k_positions(bitstring, k):
    """if the bitstring is 1001011, we want to keep the last two places,
    which is 11 intact and set previous positions to 0: (x & ((1 << k) - 1))
    because, 1<<k means there are k zeros after a 1.
    Example: 1 << 3 = 1000. 1000 - 1 = 111
    so this will keep the last k places intact and set other places to zero.
    """
    shifted_one = create_and_shift_ones(bitstring, k)  # create a bitarray of 1 and shift it left k times
    str_len = len(bitstring)  # this length doesn't include '0b'
    shifted_one_minus_one = bin(shifted_one.int - 1)[2:]  # subtract 1 from the shifted 1, so that all bits are 1s
    diff = len(bitstring) - len(shifted_one_minus_one)  # this much 0s are needed to make them of equal lenght
    equal_length_ones = BitArray('0b' + '0' * diff + shifted_one_minus_one)
    return equal_length_ones.__and__(bitstring)  # now we can perform the AND operation


if __name__ == '__main__':
    bitstr = '0b110110'
    print check_ith_bit_off(BitArray(bitstr), 3)
    print turn_ith_bit_on(BitArray(bitstr), 3)
    print toggle_ith_bit(BitArray(bitstr), 3)
    print turn_ith_bit_off(BitArray(bitstr), 3)
    print set_all_off_except_last_k_positions(BitArray(bitstr), 3)
