import sys

from data.processor import validate_path, ask_for_file_path
from utils.common import choice_menu, exit_program
from data.processor import get_values_from_file, validate_path
from utils.display import logger, custom_input, clear_terminal


# Główna funkcja

def main():
    """Run the main menu and process the selected file.

    Args:
        None: No arguments are accepted.

    Returns:
        None: This function executes the application flow and exits after processing the selected file or terminating the program.
    """

    clear_terminal()
    logger.info("MENU")
    file_path = choice_menu( 
        ("Wczytaj plik", ask_for_file_path),
        ("Wyjdź z programu", exit_program))
    
    get_values_from_file(file_path)
    
main()

