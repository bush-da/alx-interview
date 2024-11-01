#!/usr/bin/python3
"""
This module provides a function to determine if a given data set represents
a valid UTF-8 encoding.
"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    UTF-8 encoding allows characters to be represented by 1 to 4 bytes.
    The pattern of each byte in a character is defined as follows:
        - 1-byte character: 0xxxxxxx
        - 2-byte character: 110xxxxx 10xxxxxx
        - 3-byte character: 1110xxxx 10xxxxxx 10xxxxxx
        - 4-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

    Args:
    data (List[int]): A list of integers where each integer represents a byte
                      (0 to 255).

    Returns:
    bool: True if data is a valid UTF-8 encoding, False otherwise.
    """
    num_bytes = 0
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        byte = byte & 0xFF

        if num_bytes == 0:
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                continue

            if num_bytes == 1 or num_bytes > 4:
                return False
        else:
            if not (byte & mask1 and not (byte & mask2)):
                return False

        num_bytes -= 1

    return num_bytes == 0
