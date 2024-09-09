def common_difference_ap(a, b):
    """Calculates the common difference of an arithmetic progression iteratively.

      Args:
        a: The first term.
        b: The second term.

      Returns:
        float: The common difference of the arithmetic progression.
    """

    return b - a


#  Example usage:
first_term = 2
second_term = 5
result = common_difference_ap(first_term, second_term)
print(result)
