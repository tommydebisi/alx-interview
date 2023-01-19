#!/usr/bin/python3
"""
    0-stats mod
"""
import sys
import re
import signal


def handler(signal_recieved, frame, fsize_sum: int, status_list):
    """
        Handles the signal passed in
    """
    print("File size: {}".format(fsize_sum))
    print("\n".join(status_list))
    raise KeyboardInterrupt


line_count = 0
fsize_sum = 0
status_obj = dict()
regex = r"^\d.*\s\-\s\[\d*.*\]\s\"GET.*\"\s(\d*)\s(\d*)$"

for line in sys.stdin:
    if not re.search(regex, line):
        continue

    vals_needed = re.findall(regex, line)
    fsize_sum += int(vals_needed[0][1])

    status_code = int(vals_needed[0][0])
    if not status_obj.get(status_code):
        status_obj[status_code] = 0
    status_obj[status_code] += 1

    line_count += 1

    join_stat = [f"{ky}: {status_obj.get(ky)}" for ky in sorted(status_obj)]
    signal.signal(signal.SIGINT, lambda signum, frame: handler(signum, frame,
                                                               fsize_sum,
                                                               join_stat))

    if line_count == 10:
        print("File size: {}".format(fsize_sum))
        for key in sorted(status_obj):
            print("{}: {}".format(key, status_obj.get(key)))
        line_count = 0
