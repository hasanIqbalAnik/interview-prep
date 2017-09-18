"""
There are different ways to check the primality of a number. Some tests says whether a number is prime or not,
where some tests prove whether a number is composite or not. This is not a primality test but can produce primes.

Sieve of Eratosthenes is an ancient algorithm for producing a list of primes in the range n. It requires
O( n * log log n) and requires O(n) memory.

Algorithm:
1. create a bitarray of True with the size of n-1
2. each value represents a number in the range 2->n
3. starting from the beginning, which is '2' in our algorithm, make all multiples of this position to False.
4. select the next True value, which would be 3 in our case.
5. mark all multiples of 3 as False.
6. select the next True value and continue this process
7. if for some number, it's square is greater than n itself, stop the algorithm.

"""
import math


def sieve_of_eratosthenes(n):
    """
    given a number n, generate a list of primes from 2 to n.
    :param n:
    :return: list of primes
    """

    primes = [True] * (n + 1)  # extra element to match the position and the number \

    for i in range(2, int(math.sqrt(n)) + 1):
        k = 1  # the increment
        if primes[i]:
            for j in range(i*i, n+1, i*k):
                primes[j] = False
                k += 1

    print primes
print(sieve_of_eratosthenes(10))