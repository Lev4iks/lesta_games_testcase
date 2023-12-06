def isEven(value):
    """First (example) realization"""
    return value % 2 == 0


def is_even(value):
    """Second (my) realization"""
    return not value & 1
