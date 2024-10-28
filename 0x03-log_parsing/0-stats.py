#!/usr/bin/python3
"""Write a script that reads stdin line by line and
computes metrics:
"""
from typing import Union, Dict
import sys


# a function that prints a status code
def print_statictics(total_file_size: int, status_code: Dict) -> str:
    """Prints statistics and the updated count"""
    print(f"File size: {total_file_size}")

    for code, count in sorted(status_code.items()):
        print(f"{code}: {count}")


def parse_stdin(_input: str, status_codes) -> Union[int, str]:
    """Parses stdin and extract values in an array"""

    all_input = _input.split()

    # check if len(list) matches the length of args expected
    if len(all_input) >= 7:
        status_code = all_input[-2]
        file_size_str = all_input[-1]

        try:
            if status_code in status_codes:
                file_size = int(file_size_str)
                return status_code, file_size

        except ValueError as e:
            return None, None


status_codes = {
    "200": 0, "301": 0,
    "400": 0, "401": 0,
    "403": 0, "404": 0, "405": 0,
    "500": 0
}

line_count = 0
total_file_size = 0

try:
    # loop through the stdin line by line
    for line in sys.stdin:
        # increment line_count
        line_count += 1

        # Parse the line in parse_stdin function to split into
        # an array
        code, file_size = parse_stdin(line, status_codes)

        if file_size is not None and code in status_codes:
            total_file_size += file_size
            status_codes[code] += 1

        if line_count % 10 == 0:
            print_statictics(total_file_size, status_codes)
            line_count = 0
except KeyboardInterrupt:
    print_statictics(total_file_size, status_codes)
    sys.exit(0)

finally:
    print_statictics(total_file_size, status_codes)
