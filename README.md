# Research Data Compiler

A command-line tool that filters and exports research paper data from CSV files.
Built as a practical tool for research assistant work in university labs.

## What it does
- Takes any CSV file containing research data
- Filters rows by topic keyword
- Exports clean results to a new CSV file
- Handles invalid filenames by prompting until a valid file is entered
- Catches empty search results before asking for an output file

## How to run it
Make sure you have Python installed, then run:

    python compiler.py

You will be prompted to enter:
1. Your input CSV filename (re-prompted if file is not found)
2. A topic to filter by (or press Enter to show all)
3. A name for the output file (only if results are found)

## Example
Input file: data.csv
Filter: CMOS
Output: results.csv

## Error handling
- If the file does not exist, the program asks again instead of crashing
- If no rows match the filter, the program exits cleanly with a message

## Skills used
- Python
- CSV file handling
- Command line input/output
- Data filtering and export
- Error handling with loops and conditionals

## Built by
Keshav Suresh
Incoming Waterloo Nanotechnology Engineering, Fall 2026
LinkedIn: linkedin.com/in/keshav-suresh-74926b361
