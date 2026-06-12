import csv


def read_csv_rows(file_path):
    """Read CSV file and return its contents as a list of rows.

    Args:
        file_path (str): Path to the CSV file to read.

    Returns:
        list: A list of rows, where each row is a list of CSV values.
    """

    with open(file_path, encoding="utf-8") as f:
        reader = csv.reader(f)
        file_list = list(reader)
        return file_list   


def read_file_add_values_and_axis(rows):
    """Extract axis labels and column values from CSV rows.

    The first row of rows is expected to contain the x and y axis labels. Subsequent rows should contain the corresponding x and y values.

    Args:
        rows (list[list[str]]): CSV content as a list of rows, where the first row contains two strings (x axis label, y axis label) and each following row contains at least two values (x, y).

    Returns:
        tuple: A tuple of four elements (x_axis, y_axis, x_values, y_values).
    """

    x_axis, y_axis = rows[0]
    x_values = []
    y_values = []

    for row in rows[1:]:
        x_values.append(row[0])
        y_values.append(row[1])

    return x_axis, y_axis, x_values, y_values
