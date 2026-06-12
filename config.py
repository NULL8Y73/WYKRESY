
"""Application-wide configuration constants used by plotting, display, and validation logic.

Includes terminal layout percentages, ANSI color codes for status messages, and limits
for input file size and row count.
"""

CHART_X_WIDTH_PERCENT = 15
CHART_BAR_WIDTH_PERCENT = 50
LOGO_SCALE_PERCENT = 50

COLOR_INFO_TEXT = "\033[0;32m"  
COLOR_WARNING_TEXT = "\033[33m" 
COLOR_ERROR_TEXT = "\033[0;31m" 
COLOR_RESET = "\033[0m" 

FILE_SIZE_LIMIT = 5 * 1024 ** 2 
ROWS_LIMIT = 10000 

ASCII_CHARS = "@%#*+=-:. "
