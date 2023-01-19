#!/usr/bin/python3
"""
    0-stats mod
"""
import sys
import re

line_count = 0
fsize_sum = 0
status_obj = dict()
regex = r"^\d.*\s\-\s\[\d*.*\]\s\"GET.*\"\s(\d*)\s(\d*)$"

try:
    for line in sys.stdin:
        if not re.search(regex, line):
            continue

        # get status code and file size
        vals_needed = re.findall(regex, line)
        fsize_sum += int(vals_needed[0][1])
        status_code = int(vals_needed[0][0])

        if not status_obj.get(status_code):
            status_obj[status_code] = 0
        status_obj[status_code] += 1

        line_count += 1

        if line_count == 10:
            print("File size: {}".format(fsize_sum))
            for key in sorted(status_obj):
                print("{}: {}".format(key, status_obj.get(key)))
            line_count = 0

    if line_count < 10:
        print("File size: {}".format(fsize_sum))
        for key in sorted(status_obj):
            print("{}: {}".format(key, status_obj.get(key)))

except KeyboardInterrupt as e:
    res = ["File size: {}".format(fsize_sum)]
    for key in sorted(status_obj):
        res.append("{}: {}".format(key, status_obj.get(key)))
    print("\n".join(res))
    raise e
