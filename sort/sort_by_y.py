

def sort_y_increasing(x_values, y_values):
    """Return x and y sequences sorted by y in increasing order.

    Args:
        x_values (iterable): Iterable of x values to sort.
        y_values (iterable): Iterable of y values paired with x_values.

    Returns:
        tuple: A pair of tuples (x_sorted, y_sorted) where both are ordered by the corresponding y-values in ascending order.
    """

    xy_make_line = []

    for x, y in zip(x_values, y_values):
        xy_make_line.append((x, float(y)))
    
    xy_sorted = sorted(xy_make_line, key = lambda pair: pair[1])
    x_sorted, y_sorted = zip(*xy_sorted)
    return x_sorted, y_sorted


def sort_y_decreasing(x_values, y_values):
    """Return x and y sequences sorted by y in decreasing order.

    Args:
        x_values (iterable): Iterable of x values to sort.
        y_values (iterable): Iterable of y values paired with x_values.

    Returns:
        tuple: A pair of tuples (x_sorted, y_sorted) where both are ordered by the corresponding y-values in descending order.
    """

    xy_make_line = []

    for x, y in zip(x_values, y_values):
        xy_make_line.append((x, float(y)))
    
    xy_sorted = sorted(xy_make_line, key = lambda pair: pair[1], reverse = True)
    x_sorted, y_sorted = zip(*xy_sorted)
    return x_sorted, y_sorted