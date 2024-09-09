def sum_ap(a, d, n):
    """Calculates the sum term of an arithmetic progression iteratively.

      Args:
        a: The first term.
        d: The common difference.
        n: The position of the term to calculate.

      Returns:
        float: The sum term of the arithmetic progression.
    """

    return n / 2 * (2 * a + (n-1) * d)


#  Example usage:
first_term = 2
common_difference = 3
term_number = 5
result = sum_ap(first_term, common_difference, term_number)
print(result)
