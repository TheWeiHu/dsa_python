"""
References
Lucia Moura's CSI 2110 Chapter 19 Course Notes
Not only better in terms of its implementation, but also its legibility compared to
the nonsense found here:
https://www.geeksforgeeks.org/boyer-moore-algorithm-for-pattern-searching/

Given a pattern, and an input string, give all the indices after which the pattern can
be found.

Example:
    Given input_string = "ABBCDDBCE", pattern = "BC",
    Because input_string[2:4] == input_string[6,8]
    return 2,6
"""


def preprocess(pattern):
    """
    Note the last occurence index of each character in the pattern.
    time: O(m)
    space: O(m)
    where m is the size of the pattern.
    """
    result = {}
    for index, element in enumerate(pattern):
        result[element] = index
    return result


def boyer_moore(input_string, pattern):
    """
    time: O(mn)
    space: O(m)
    note although the upperbound is the same as the brute force solution, it performs
    better regardless of the input.
    """
    last_occurence = preprocess(pattern)
    i = j = len(pattern) - 1
    while i <= len(input_string) - 1:
        # Match as many characters as possible, starting from the rear of the pattern.
        if input_string[i] == pattern[j]:
            if j == 0:
                # All characters match!
                yield i
                # Restart algorithm starting right after the matched string.
                i = i + len(pattern)
                j = len(pattern) - 1
            else:
                i -= 1
                j -= 1
        else:
            # If the mismatched character appears in the pattern, then we allign the
            # last occurence of the character in the pattern with the mismatched
            # location. Else, we start over, the index after the mismatched character.
            i += len(pattern) - min(j, 1 + last_occurence.get(input_string[i], -1))
            j = len(pattern) - 1
            # Note: a minumum of j guarrantees we do not move so far back that we start
            # matching again from a section we've already eliminated.