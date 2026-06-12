from dateutil import parser
from datetime import datetime


def sort_x_increasing(x_values, y_values, data_type):
    """Sort paired x and y values by x in increasing order.

    Args:
        x_values (iterable): Iterable of x values to sort.
        y_values (iterable): Iterable of y values paired with x_values.
        data_type (str): One of "float", "str", or "date". Dates must use DD.MM.YYYY.

    Returns:
        tuple: A tuple of two sequences: (x_sorted, y_sorted) with items reordered by x.
    """

    xy_make_line = []

    for x, y in zip(x_values, y_values):
        xy_make_line.append((x, y))
    
    if data_type == "float":
        xy_sorted = sorted(xy_make_line, key = lambda pair: float(pair[0]))

    elif data_type == "str":
        xy_sorted = sorted(xy_make_line, key = lambda pair: str(pair[0]))

    elif data_type == "date":
        xy_sorted = sorted(xy_make_line, key=lambda pair: datetime.strptime(str(pair[0]).strip(), "%d.%m.%Y"))

    x_sorted, y_sorted = zip(*xy_sorted)
    return x_sorted, y_sorted


def sort_x_decreasing(x_values, y_values, data_type):
    """Sort paired x and y values by x in decreasing order.

    Args:
        x_values (iterable): Iterable of x values to sort.
        y_values (iterable): Iterable of y values paired with x_values.
        data_type (str): One of "float", "str", or "date". Dates must use DD.MM.YYYY.

    Returns:
        tuple: A tuple of two sequences: (x_sorted, y_sorted) with items reordered by x descending.
    """

    xy_make_line = []

    for x, y in zip(x_values, y_values):
        xy_make_line.append((x, y))

    if data_type == "float":
        xy_sorted = sorted(xy_make_line, key = lambda pair: float(pair[0]), reverse = True)

    elif data_type == "str":
        xy_sorted = sorted(xy_make_line, key = lambda pair: str(pair[0]), reverse = True)

    elif data_type == "date":
        xy_sorted = sorted(xy_make_line, key=lambda pair: datetime.strptime(str(pair[0]).strip(), "%d.%m.%Y"), reverse = True)

    x_sorted, y_sorted = zip(*xy_sorted)
    return x_sorted, y_sorted