import os  # BUG: LINTING - Unused import 'os'
import sys

def calculate_area(radius) # BUG: SYNTAX - Missing colon
    if radius < 0:
        return 0
    return 3.14 * (radius ** 2)