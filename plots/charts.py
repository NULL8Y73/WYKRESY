import shutil

from utils.common import set_width_for_elements
from config import CHART_X_WIDTH_PERCENT, CHART_BAR_WIDTH_PERCENT
from utils.common import set_width_for_elements
from utils.display import logger


def show_block(list_to_display):
    """Center each line in list_to_display and log the result.

    Args:
        list_to_display (list[str]): Lines to center and display.

    Returns:
        None: No return value.
    """

    terminal_width = shutil.get_terminal_size().columns
    max_len = max(len(l) for l in list_to_display)
    margin = " " * ((terminal_width - max_len) // 2)
    block = "\n".join(f"{margin}{line}" for line in list_to_display)

    logger.info(block)


def charts_generator(x_values_chart, y_value_chart):
    """Generate textual bar-chart lines from X and Y data.

    Args:
        x_values_chart (list[str]): Labels for each bar.
        y_value_chart (list[float]): Numeric values corresponding to each label.

    Returns:
        list[str]: Lines representing the chart, suitable for logging or printing.
    """

    x_width = set_width_for_elements(CHART_X_WIDTH_PERCENT)
    bar_width = set_width_for_elements(CHART_BAR_WIDTH_PERCENT)
    x_width_int = int(x_width)

    y_value_chart = list(map(float, y_value_chart))

    lines = []
    max_value_y = max(y_value_chart)
    min_value_y = min(y_value_chart)
    chart_fragment = "▃"

    for x, y in zip(x_values_chart, y_value_chart):
        float_y_chart_width = (y - min_value_y)/(max_value_y - (min_value_y)) * bar_width
        y_width_int = int(float_y_chart_width)

        if len(x) > x_width_int:
            x = x[:x_width_int - 3] + "..."
        
        x = x.ljust(x_width_int)
        padding = " " * int(bar_width - y_width_int)
        
        lines.append(f"{x}: {y_width_int * chart_fragment}{padding} {y}")

    return lines
        

   