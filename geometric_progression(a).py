def sum_gp(a, r, n):
    """Calculates the sum term of a geometric progression iteratively.

  Args:
    a: The first term.
    r: The common ratio.
    n: The number of terms.

  Returns:
    float: The sum term of the first n terms of the geometric progression.
    :param r:
    :param a:
    :param n:
"""

    if r ^ 1:
        return a * n
    else:
        return a * (1 - r ** n) / (1 - r)


#  Example usage:
first_term = 2
common_ratio = 2
term_number = 5
result = sum_gp(first_term, common_ratio, term_number)
print(result)
