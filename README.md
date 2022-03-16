# fractioncalc

![language:Python](https://img.shields.io/badge/Language-Python-blue.svg?style=flat-square) ![license:MIT](https://img.shields.io/badge/License-MIT-green.svg?style=flat-square) 

## Python terminal application for calculating fractional arithmetic.

## Requirements:
1. Python 3.10 https://www.python.org/downloads/

## Install:
1. Download this repo as a zip and extract to a directory of your choice.

## To Run: 
1. Open a terminal and make sure python is in the PATH 
2. In the command line, navigate to the installed directory
3. Type py fractioncalc.py

## Files:
1. fractioncalc.py, python application
2. testData.py, import file for testing the reduce() function in fractioncalc.py
3. TestData.xslx Excel workbook for generating some test data

## About this application
*Upon running, the user will be prompted to enter in a fractinoal arithmetic problem with one operator and two operands.
*The user may enter '?' for instructions or 'Q' to quit at any time.
*Valid inputs are positive or negative, whole, fractional (proper or imporper), or mixed numbers. 
*No decimals are allowed. 
*Negative signs must lead the entire operand and there must be no whitespace between the sign and the number.
*Fractions are reduced by finding prime factors then comparing them to find the GCD.
*If the user types 'test' a propt for unit testing will appear. Once the test is run, the application will quit.

## TO DO:
1. Option A: Set a limit on denominator size to avoid very long calculation times for numbers with very large denominators (~10^9)
2. OPtion B: Warn user they might be waiting a while or have a time-out function. 
3. Program should handle n number of terms and follow PEMDAS
4. Program should handle parentheses and exponents
