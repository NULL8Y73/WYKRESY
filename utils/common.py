import shutil
import sys

from utils.display import logger, custom_input, clear_terminal
from PIL import Image


def exit_program():
    """Exit the application immediately.

    Returns:
        None: Does not return normally.
    """

    sys.exit()


def check_input_problems(input_checking, expected_type):
    """Validate and convert user input to an expected type.

    Args:
        input_checking (Any): The value to validate and convert.
        expected_type (type): The target type for conversion (for example, int or float).

    Returns:
        Any: The converted value if conversion succeeds; otherwise None.
    """

    try:
        checking_result = expected_type(input_checking)
        return checking_result
    except ValueError:
        return None
    

def choice_menu(*options):
    """Display a numbered menu and execute the selected action.

    Args:
        *options (tuple): Each option is a tuple of (label, callback), where label is a string shown to the user and callback is a callable executed for that option.

    Returns:
        Any: The return value of the selected option callback.
    """

    while True:
        for option_number, (label, _) in enumerate(options, 1):
            logger.info(f"{option_number}. {label}")

        select_option = custom_input("Wybierz opcje: ")
        input_result = check_input_problems(select_option, int)

        if input_result is None:
            clear_terminal()
            logger.error("Podano wartość, która nie jest samą liczbą lub jest innym typem niż liczba")
            continue

        selection_index = input_result - 1

        if selection_index < 0 or selection_index >= len(options):
            clear_terminal()
            logger.error("Dana opcja nie istnieje. ")
            continue

        return options[selection_index][1]()
    

def set_width_for_elements(width_percent_for_elements):
    """Calculate terminal width for elements by percentage.

    Args:
        width_percent_for_elements (float): Percentage of terminal width to allocate.

    Returns:
        float: The width in terminal columns corresponding to the given percentage.
    """

    terminal_width = shutil.get_terminal_size().columns

    elements_width_in_terminal = terminal_width * width_percent_for_elements / 100
    
    return elements_width_in_terminal

