"""
The following code finds all possible permutations in two different  methods.
The algorithm works as follows:
1. if there is only one character in that string, then the permutation is itself. This is the base case.
2. else, that character should precede the permutations of the remaining characters.

Time Complexity: O(n*n!) (though i don't know how)
"""


def permutations_recursive(s):
    results = []
    if s:
        if len(s) == 1:
            return [s]
        else:
            for ch in s:
                p = permutations_recursive(''.join([x for x in s if x != ch]))
                for item in p:
                    results.append(ch + item)
    return results

print permutations_recursive('abc')
