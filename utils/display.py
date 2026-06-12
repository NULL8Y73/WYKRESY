import shutil
import logging
import os

from PIL import Image

from config import (
    COLOR_INFO_TEXT, COLOR_WARNING_TEXT, 
    COLOR_ERROR_TEXT, COLOR_RESET,
    ASCII_CHARS, LOGO_SCALE_PERCENT
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
    

def convert_photo_to_ascii(photo_path, photo_expected_scale):
    """Convert an image file to ASCII art.

    Args:
        photo_path (str): The file path to the image to convert.
        photo_expected_scale (int): The desired width of the ASCII art in percentage.

    Returns:
        str: A string containing the ASCII art representation of the image.
    """

    from utils.common import set_width_for_elements

    image_before_conversion = Image.open(photo_path)
    image_width, image_height = image_before_conversion.size

    set_image_monohrome = image_before_conversion.convert("L")

    scale_for_photo_ascii = set_width_for_elements(photo_expected_scale)

    image_new_width = int(scale_for_photo_ascii)
    image_new_height = int(scale_for_photo_ascii * (image_height / image_width) * 0.55)
    
    image_ascii_size = set_image_monohrome.resize((image_new_width, image_new_height))

    all_pixels = image_ascii_size.getdata()

    ascii_image = ""

    for pixel in all_pixels:
        change_pixel_to_ascii = int(pixel * len(ASCII_CHARS) // 256)
        ascii_image += ASCII_CHARS[change_pixel_to_ascii]
    
    final_ascii_image = ""

    for line_start in range(0, len(ascii_image), image_new_width):
        raw_line = ascii_image[line_start: line_start + image_new_width]
        centered_line = center_text(raw_line)
        final_ascii_image += centered_line + "\n"

    centered_ascii_image = center_text(final_ascii_image)

    logger.info(centered_ascii_image)

    return centered_ascii_image


def base_screen():
    """Display the base screen with a centered logo.

    Returns:
        None: Does not return a value.
    """

    clear_terminal()
    convert_photo_to_ascii("assets/wykresy_logo.png", LOGO_SCALE_PERCENT)