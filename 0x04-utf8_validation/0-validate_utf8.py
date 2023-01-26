#!/usr/bin/python3
"""
    validate_utf8 mod
"""


def validUTF8(data):
    """
        determines if a given data set represents a valid UTF-8 encoding.
        returns true if valid or false if not
    """
    byte_num = 0
    for elem in data:
        bin_str = bin(elem)[2:]

        if len(bin_str) > 8:
            bin_str = bin_str[(len(bin_str) - 8):]

        if len(bin_str) < 8:
            if byte_num != 0:
                return False
        else:
            if byte_num == 0:
                if bin_str.startswith('10'):
                    return False

                for ints in bin_str:
                    if byte_num == 5:
                        return False

                    if ints == '0':
                        break
                    byte_num += 1
                byte_num -= 1
            else:
                if not bin_str.startswith('10'):
                    return False
                byte_num -= 1
    if byte_num != 0:
        return False
    return True
