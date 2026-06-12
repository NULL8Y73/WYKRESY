# Wykresy
**Author:** Nela Popławska

## Description

**Wykresy** is a Python console application that loads two-column CSV datasets, validates the file structure, and displays an interactive chart-like view in the terminal. The project supports sorting by the first or second column and lets users explore data in ascending or descending order, while protecting against invalid file paths, unsupported formats, large files, and malformed rows.

## Features

- Interactive terminal menu for file selection and program navigation
- Validates CSV input with checks for:
  - file existence and path correctness
  - file type and `.csv` extension
  - maximum file size and row limits
  - consistent row/column format
  - numeric values in the second column
- Reads axis labels from the first CSV row and extracts x/y values from subsequent rows
- Supports sorting chart data by:
  - first column (x-axis) ascending or descending
  - second column (y-axis) ascending or descending
- Automatically detects data type for the first column, including string, date, and numeric values
- Clean terminal UI with centered messages and color-coded logging

## Tech Stack

- Python
- Standard library modules: `csv`, `os`, `logging`, `shutil`, `sys`
- Third-party library:
  - `python-dateutil` for date parsing in data validation

## Prerequisites & Installation

1. Clone the repository:

```bash
git clone <repository-url>
cd Wykresy
```

2. Create and activate a Python virtual environment (recommended):

```bash
python -m venv venv
venv\Scripts\activate
```

3. Install dependencies:

```bash
pip install python-dateutil
```

4. No additional environment variables are required for this project.

## Usage

1. Run the application from the project root:

```bash
python main.py
```

2. Follow the on-screen menu to:

- load a CSV file by entering its path
- choose between sorting the chart data by the first or second column
- exit the program

## CSV Input Format

The CSV file must contain:

- a header row with two labels (x-axis label and y-axis label)
- subsequent rows with at least two values
- numeric values in the second column

Example:

```csv
Date,Value
2024-01-01,100
2024-01-02,150
```

## Project Structure

- `main.py` — application entry point and menu
- `config.py` — application constants and settings
- `validation.py` — file and data validation helpers
- `data/loader.py` — CSV reading and row parsing
- `data/processor.py` — data extraction and validation
- `plots/charts.py` — chart rendering utilities
- `sort/sort_by_x.py` — x-axis sorting logic
- `sort/sort_by_y.py` — y-axis sorting logic
- `utils/common.py` — core menu and input helpers
- `utils/display.py` — terminal rendering, logging, and input handling

## Notes

- Keep CSV files within reasonable size limits to avoid validation failures.
- The application is designed for two-column CSV datasets and expects the second column to be numeric.
