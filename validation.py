import os
import csv

from dateutil import parser

from data.loader import read_csv_rows


def validate_path_is_exist(file_path):
    """Check whether a file path exists.

    Args:
        file_path (str): Path to the file or directory.

    Returns:
        bool: True if the path exists, otherwise False.
    """

    file_path_exist = os.path.exists(file_path)
    return file_path_exist


def validate_path_is_folder(file_path):
    """Check whether a path points to a regular file.

    Args:
        file_path (str): Path to the file to check.

    Returns:
        bool: True if the path is a regular file, otherwise False.
    """

    file_path_is_folder = os.path.isfile(file_path)
    return file_path_is_folder


def validate_path_extension(file_path):
    """Return the file extension for a path.

    Args:
        file_path (str): Path to the file.

    Returns:
        str: File extension including the leading dot, or an empty string if none.
    """

    split_file = os.path.splitext(file_path)
    file_extension = split_file[1]
    return file_extension


def validate_check_size_of_file(file_path):
    """Return the size of a file in bytes.

    Args:
        file_path (str): Path to the file.

    Returns:
        int: File size in bytes.
    """
    
    file_size = os.path.getsize(file_path)
    return file_size


def validate_check_rows_number(rows):
    """Return the number of rows in a dataset.

    Args:
        rows (list): List of rows, typically read from a CSV file.

    Returns:
        int: Number of rows.
    """

    rows_numebr = len(rows)
    return rows_numebr


def validate_file_is_full(rows):
    """Validate whether a dataset contains at least one row.

    Args:
        rows (list): List of rows, where the first row is expected to be header columns.

    Returns:
        bool: True if the rows list is non-empty, otherwise False.
    """

    try:
        columns = rows[0]
    except IndexError:
        return False
    return True


def validate_file_rows(rows):
    """Validate that all data rows have the same number of columns as the header.

    Args:
        rows (list): List of rows, where the first row is header columns.

    Returns:
        int or bool: Number of columns if all rows match the header length, otherwise False.
    """

    columns = rows[0]
    columns_number = len(columns)

    for row in rows[1:]:
        if len(row) != columns_number:
            return False

    return columns_number


def validate_file_type(rows):
    """Validate that the second column of each row can be converted to float.

    Args:
        rows (list): List of rows, where each row contains at least two columns.

    Returns:
        bool: True if all rows have a numeric second column, otherwise False.
    """

    for row in rows[1:]:
        try:
            float(row[1])
        except ValueError:
            return False
    return True


def validate_data_type(rows):
    """Infer the data type of the first column for each row.

    Args:
        rows (list): List of rows, where each row has at least one column.

    Returns:
        list[str]: Data type labels for each row after the header.
    """

    data_types_in_all_rows = []
    for row in rows[1:]:
        data_type = ""
        
        if type(row[0]) == str:
            try:
                parser.parse(row[0])
                data_type = "date"
            except ValueError:
                data_type = "str"
            
        if type(row[0]) == int:
            data_type = "int"
        
        if type(row[0]) == float:
            data_type = "float"

        if type(row[0]) == bool:
            data_type = "bool"

        data_types_in_all_rows.append(data_type)
        
    return data_types_in_all_rows

        