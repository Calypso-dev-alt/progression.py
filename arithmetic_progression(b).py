def nth_term_ap(a, d, n):
    """Calculates the nth term of an arithmetic progression iteratively.

      Args:
        a: The first term.
        d: The common difference.
        n: The position of the term to calculate.

      Returns:
        float: The nth term of the arithmetic progression.
    """

    return a + (n - 1) * d


#  Example usage:
first_term = 2
common_difference = 3
term_number = 7
result = nth_term_ap(first_term, common_difference, term_number)
print(result)
