def nth_term_gp(a, r, n):
    """Calculates the nth term of a geometric progression iteratively.

      Args:
        a: The first term.
        r: The common ratio.
        n: The number of terms.

      Returns:
        float: The nth term of the arithmetic progression.
    """

    return a * (r ** (n - 1))


#  Example usage:
first_term = 2
common_ratio = 3
term_number = 7
result = nth_term_gp(first_term, common_ratio, term_number)
print(result)
