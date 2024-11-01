#!/usr/bin/env python3
"""Utf-8 validation"""


def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.

    UTF-8 encoding can have characters represented by 1 to 4 bytes.
    Each byte follows specific patterns based on the length of the character:
        - 1-byte character: 0xxxxxxx
        - 2-byte character: 110xxxxx 10xxxxxx
        - 3-byte character: 1110xxxx 10xxxxxx 10xxxxxx
        - 4-byte character: 11110xxx 10xxxxxx 10xxxxxx 10xxxxxx

    Args:
    data (List[int]): A list of integers where each integer
    represents a byte of data.
                      Each integer is assumed to be within the
    range of an 8-bit byte (0 to 255).

    Returns:
    bool: True if the data set represents a valid UTF-8 encoding,
    False otherwise.
    """
    # Number of bytes in the current UTF-8 character
    num_bytes = 0

    # Masks to check the initial bits in a byte
    mask1 = 1 << 7  # 10000000
    mask2 = 1 << 6  # 01000000

    for byte in data:
        # Mask to get only the least significant 8 bits
        byte = byte & 0xFF

        if num_bytes == 0:
            # Determine the number of bytes based on the leading 1's
            mask = 1 << 7
            while mask & byte:
                num_bytes += 1
                mask = mask >> 1

            if num_bytes == 0:
                # 1-byte character
                continue

            if num_bytes == 1 or num_bytes > 4:
                # Invalid UTF-8 (1 leading bit or more than 4 leading bits)
                return False
        else:
            # Continuation byte must start with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        # Decrease the number of bytes needed for the character
        num_bytes -= 1

    return num_bytes == 0
