# fractioncalc

![language:Python](https://img.shields.io/badge/Language-Python-blue.svg?style=flat-square) ![license:MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square) 

## Python terminal application for calculating fractional arithmetic.

## Requirements:
1. [Python 3.10](https://www.python.org/downloads/)

## Install:
1. Download this repository as a zip and extract to a directory of your choice.

## To Run: 
1. Open a terminal and make sure python is in the PATH. 
2. In the command line, navigate to the installed directory.
3. In the command line, type:
    ```py fractioncalc.py```

## Files:
1. fractioncalc.py
   - Python application file.
2. testData.py
   - Imported for testing the reduce() function in fractioncalc.py.
3. TestData.xslx
   - An Excel workbook for generating some test data.
4. readme.md

## About this application
- Upon running, the user will be prompted to enter in a fractional arithmetic problem with one operator and two operands.
- The user may enter '?' for instructions or 'Q' to quit at any time.
- Valid inputs are positive or negative, whole, fractional (proper or improper), or mixed numbers. 
- No decimals are allowed. 
- Negative signs must lead the entire operand and there must be no whitespace between the sign and the number.
- Fractions are reduced by finding prime factors then comparing them to find the GCD.
- If the user types 'test' a prompt for unit testing will appear. Once the test is run, the application will quit.

## TO DO:
1. Deal with the case of finding the LCD of very large numerators and denominators (~10^9).
   - Option A: Set a limit on denominator size.
   - Option B: Warn user they might be waiting a while or have a time-out/display percentage function. 
2. Program should handle n number of terms and follow PEMDAS.
3. Program should handle parentheses and exponents.
