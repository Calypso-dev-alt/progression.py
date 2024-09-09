def common_ratio_gp(a, b):
    """Calculates the nth term of a geometric progression iteratively.

      Args:
        a: The first term.
        b: The second term

      Returns:
        float: The common ratio of the geometric progression.
    """

    return b / a


#  Example usage:
first_term = 2
second_term = 4
result = common_ratio_gp(first_term, second_term)
print(result)
