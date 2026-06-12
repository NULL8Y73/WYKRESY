from plots.charts import charts_generator, show_block
from data.loader import read_csv_rows, read_file_add_values_and_axis
from sort.sort_by_x import (
    sort_x_increasing, sort_x_decreasing
    )
from sort.sort_by_y import (
    sort_y_increasing, sort_y_decreasing
    )
from utils.common import choice_menu, exit_program
from utils.display import logger, clear_terminal, custom_input
from validation import (
    validate_path_is_exist, validate_path_is_folder, 
    validate_path_extension, validate_file_is_full, 
    validate_file_rows, validate_file_type,
    validate_check_rows_number, validate_check_size_of_file,
    validate_data_type
)
from config import FILE_SIZE_LIMIT, ROWS_LIMIT



def ask_for_file_path():
    """Prompt user for a file path and validate it.

    Continuously asks the user for a file path until a valid CSV file is provided.
    Validates the path using validate_path() function.

    Args:
        None: No arguments are accepted.

    Returns:
        str: A valid file path to a CSV file.
    """

    while True:
        file_path_input = custom_input("Podaj ścieżkę pliku:")

        if validate_path(file_path_input):
            return file_path_input


def set_data_type_to_values(rows):
    """Determine the appropriate data type for the dataset values.

    Analyzes the data types present in the rows and determines the most appropriate data type to use for sorting and processing.

    Args:
        rows (list): List of rows from the CSV file to analyze.

    Returns:
        str: One of 'str', 'date', or 'float' representing the determined data type.
    """

    data_types_list = validate_data_type(rows)
    unique_types = set(data_types_list)

    if "str" in unique_types or "bool" in unique_types:
        return "str"
    
    if "date" in unique_types and len(unique_types) > 1:
        return "str"

    if unique_types == {"date"}:
        return "date"

    if "float" in unique_types or "int" in unique_types:
        return "float"

    else:
        logger.error("Nie poprawne dane.")
    
    return "str"


def get_values_from_file(file_path):
    """Load data from a CSV file and display it with an interactive chart menu.

    Reads the CSV file from the given path, extracts x and y values, and displays them in a chart with sorting and navigation options.

    Args:
        file_path (str): Path to the CSV file to load.

    Returns:
        None: No return value.
    """

    read_file = read_csv_rows(file_path)
    x_axis, y_axis, x_values, y_values  = read_file_add_values_and_axis(read_file)
    display_chart_with_menu(x_values, y_values, read_file)



def display_chart_with_menu(x_values, y_values, rows):
    """Display chart with interactive sorting menu.

    Shows a chart visualization of the data and provides a menu for sorting the data by x-axis or y-axis in ascending or descending order.

    Args:
        x_values (list): Values for the x-axis.
        y_values (list): Values for the y-axis.
        rows (list): Original rows from the CSV file.

    Returns:
        None: No return value.
    """
    
    data_type_to_sort = set_data_type_to_values(rows)

    while True:
        clear_terminal()

        charts = charts_generator(x_values, y_values)
        show_block(charts)

        def open_sort_menu():


            def apply_sort_x(sorting_function):
                nonlocal x_values, y_values, data_type_to_sort
                x_values, y_values = sorting_function(x_values, y_values, data_type_to_sort)


            def apply_sort_y(sorting_function):
                nonlocal x_values, y_values
                x_values, y_values = sorting_function(x_values, y_values)

            choice_menu(
                ("Posortuj dane ROSNĄCO bazując na PIERWSZEJ kolumnie.", lambda: apply_sort_x(sort_x_increasing)),
                ("Posortuj dane MALEJĄCO bazując na PIERWSZEJ kolumnie.", lambda: apply_sort_x(sort_x_decreasing)),
                ("Posortuj dane ROSNĄCO bazując na DRUGIEJ kolumnie.", lambda: apply_sort_y(sort_y_increasing)),
                ("Posortuj dane MALEJĄCO bazując na DRUGIEJ kolumnie.", lambda: apply_sort_y(sort_y_decreasing)),
                ("Opuść program", exit_program)
            )

        choice_menu(
            ("Posortuj dane na wykresie", open_sort_menu),
            ("Opuść program", exit_program)
        )


def validate_csv_file_charts(read_file):
    """Validate CSV file format and content for chart generation.

    Performs comprehensive validation including row count, file content, column count, and data types in the second column.

    Args:
        read_file (list): List of rows from the CSV file.

    Returns:
        bool: True if file is valid for chart generation, False otherwise.
    """

    rows_number = validate_check_rows_number(read_file)
    if rows_number > ROWS_LIMIT:
        clear_terminal()
        logger.error(f"Przekroczono limit wierszy (liczba wierszy w pliku: {rows_number}, limit: {ROWS_LIMIT})")
        return False

    if validate_file_is_full(read_file) == False:
        clear_terminal()
        logger.error("Plik jest pusty.")
        return False
    
    if validate_file_rows(read_file) != 2:
        clear_terminal()
        logger.error("Plik powinien zawierać 2 kolumny danych.")
        return False
    
    if validate_file_type(read_file) == False:
        clear_terminal()
        logger.error("Druga kolumna powinna zawierać jedynie liczby całkowite lub zmiennoprzecinkowe.")
        return False

    return True


def validate_path(file_path):
    """Validate file path and CSV file for chart processing.
    
    Performs validation checks on the file path including existence, file type,
    extension, file size, and CSV content structure.
    
    Args:
        file_path (str): Path to the file to validate.
    
    Returns:
        bool: True if file path and content are valid, False otherwise.
    """
    
    if validate_path_is_exist(file_path) == False:
        clear_terminal()
        logger.error("Podano nie poprawną ścieżkę.")
        return False
    
    if validate_path_is_folder(file_path) == False:
        clear_terminal()
        logger.error("Wybrano folder zamiast pliku.")
        return False
    
    if validate_path_extension(file_path) != ".csv":
        clear_terminal()
        logger.error("Podano błędny foramt pliku.")
        return False
    
    if validate_check_size_of_file(file_path) > FILE_SIZE_LIMIT:
        clear_terminal()
        logger.error(f"Rozmiar pliku nie może przekraczać {FILE_SIZE_LIMIT} MB.")
        return False

    read_file = read_csv_rows(file_path)
    return validate_csv_file_charts(read_file)

