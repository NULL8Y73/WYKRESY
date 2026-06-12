import shutil
import logging
import os


from config import (
    COLOR_INFO_TEXT, COLOR_WARNING_TEXT, 
    COLOR_ERROR_TEXT, COLOR_RESET
)


def center_text(text):
    """Center text horizontally in the current terminal width.

    Args:
        text (str): The string to center.

    Returns:
        str: The centered text padded to the terminal width.
    """
    terminal_width = shutil.get_terminal_size().columns
    
    return text.center(terminal_width)


class CustomFormatter(logging.StreamHandler):
    """Logging handler that formats messages with terminal colors and center alignment."""

    def emit(self, record):
        """Emit a log record with colored, centered output.

        Args:
            record (logging.LogRecord): The log record to format and print.

        Returns:
            None: Does not return a value.
        """
        text_color = COLOR_RESET

        match record.levelno:
            case logging.INFO:  text_color = COLOR_INFO_TEXT
            case logging.WARNING:   text_color = COLOR_WARNING_TEXT
            case logging.ERROR: text_color = COLOR_ERROR_TEXT
        
        centered = center_text(record.getMessage())
        print(f"{text_color}{centered}{COLOR_RESET}")

logger = logging.getLogger("app")
logger.setLevel(logging.DEBUG)
logger.addHandler(CustomFormatter())


def custom_input(text):
    """Prompt the user with a centered input symbol and log the prompt message.

    Args:
        text (str): The prompt message to display and log.

    Returns:
        str: The user input string.
    """
    logger.info(text)

    symbol_input = center_text("❭❭❭")
    new_input = input(symbol_input.rstrip())
    return new_input


def clear_terminal():
    """Clear the terminal screen for the current operating system.

    Returns:
        str | None: The OS name when unsupported, otherwise None.
    """
    if os.name == "nt":
        os.system("cls")
    elif os.name == "posix":
        os.system("clear")
    else:
        return os.name