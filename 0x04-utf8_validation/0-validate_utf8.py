#!/usr/bin/python3
"""Write a method that determines if a given data
set represents a valid UTF-8 encoding.
"""
from typing import ByteString


def validUTF8(data: ByteString):
    """Return: True if data is a valid UTF-8 encoding, else return False
    A character in UTF-8 can be 1 to 4 bytes long
    The data set can contain multiple characters
    The data will be represented by a list of integers
    Each integer represents 1 byte of data, therefore you only need to
    handle the 8 least significant bits of each integer
    """

    # a check when a byte we are epecting to match is
    byte_to_expect = 0

    for ob in data:
        byte = ob & 0xFF

        if byte_to_expect == 0:

            if (byte >> 7) == 0b0:
                byte_to_expect = 0

            elif (byte >> 5) == 0b110:
                byte_to_expect = 1

            elif (byte >> 4) == 0b1110:
                byte_to_expect = 2

            elif (byte >> 3) == 0b11110:
                byte_to_expect = 3

            else:
                return False

        else:
            if (byte >> 6) != 0b10:
                return False

            byte_to_expect -= 1

    return byte_to_expect == 0
