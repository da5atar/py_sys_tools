# Change Logs

## [1.0.0] - 2024-05-06:
- Initial release
- Refactor process_tree_python_2.py to process_tree_python3.py:
  - Key Changes and Enhancements:
    Python 3 Compatibility: Updated syntax for Python 3, especially the subprocess call which now includes text=True to ensure that outputs are returned as strings.
    Improved Code Documentation: Added docstrings and inline comments to explain the purpose and functionality of each function and significant block of code.
    Regex Adjustment: Modified regex usage to ensure that the prefix is correctly updated.
    Code Simplification: Minor adjustments to simplify and clarify variable names and structures.
    Function Names: Changed psaxo to get_process_info and hieraPrint to print_hierarchy to reflect their purposes more clearly.
    Variable Names: Renamed pidpool to processes for clarity, and cmd to command to avoid abbreviation. Similarly, changed ppid to parent_pid, pppid to grandparent_pid, and pname to process_name.
    Structure: Revised some of the in-line comments and structure for better clarity.
