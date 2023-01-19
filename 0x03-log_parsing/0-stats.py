#!/usr/bin/python3
"""
    0-stats mod
"""
import sys

if __name__ == "__main__":
    line_count = 0
    fsize_sum = 0
    status_obj = dict()
    regex = r"^\d.*\s\-\s\[\d*.*\]\s\"GET.*\"\s(\d*)\s(\d*)$"
    stat_codes = [200, 301, 400, 401, 403, 404, 405, 500]

    def report_message(file_size, status_obj):
        """
            prints the format message to screen
        """
        print("File size: {}".format(file_size))
        for key, val in sorted(status_obj.items()):
            print("{}: {}".format(key, val))

    try:
        for line in sys.stdin:
            line_count += 1
            try:
                # get status code and file size
                vals_needed = line.split(" ")
                fsize_sum += int(vals_needed[-1])
                status_code = int(vals_needed[-2])

                # check if status code is part of possible codes
                if status_code in stat_codes:
                    if not status_obj.get(status_code):
                        status_obj[status_code] = 0
                    status_obj[status_code] += 1
            except (IndexError, ValueError):
                pass

            if line_count == 10:
                report_message(fsize_sum, status_obj)
                line_count = 0

        report_message(fsize_sum, status_obj)
    except KeyboardInterrupt:
        report_message(fsize_sum, status_obj)
        raise
