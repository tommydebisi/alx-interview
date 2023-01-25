#!/usr/bin/python3
"""
    validate_utf8 mod
"""


def validUTF8(data):
    """
        determines if a given data set represents a valid UTF-8 encoding.
        returns true if valid or false if not
    """
    for val in data:
        # get binary string
        bin_s = bin(val)[2:]

        if len(bin_s) > 8:
            bin_s = bin_s[(len(bin_s) - 8):]

        if not bin_s.startswith('1') or '1' not in bin_s or '0' not in bin_s:
            return False

    return True
