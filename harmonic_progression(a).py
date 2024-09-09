def nth_term_hp(a, d, n):
    """Calculates the nth term of a harmonic progression iteratively.

  Args:
    a: The first term.
    d: The common difference.
    n: The term number.

  Returns:
    float: The nth term of the harmonic progression.
    :param a:
    :param d:
    :param n:
    :return:
"""

    return 1 / (a + (n - 1) * d)


#  Example usage:
first_term = 1
common_difference = 1
term_number = 10
result = nth_term_hp(first_term, common_difference, term_number)
print(result)
