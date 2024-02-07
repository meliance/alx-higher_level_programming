#!/usr/bin/python3
"""Reads from standard input and computes metrics.
After every ten lines or the input of a keyboard interruption (CTRL + C),
prints the following statistics:
    - Total file size up to that point.
    - Count of read status codes up to that point.
"""

def print_statistics(total_size, status_codes):
    """
    Prints the statistics computed from the accumulated data.
    """
    print("File size: {}".format(total_size))
    sorted_status_codes = sorted(status_codes.items())
    for code, count in sorted_status_codes:
        print("{}: {}".format(code, count))

def main():
    total_size = 0
    status_codes = {'200': 0, '301': 0, '400': 0, '401': 0, '403': 0, '404': 0, '405': 0, '500': 0}
    line_count = 0

    try:
        for line in sys.stdin:
            line_count += 1
            parts = line.split()
            if len(parts) >= 2:
                status_code = parts[-2]
                file_size = int(parts[-1])
                total_size += file_size
                if status_code in status_codes:
                    status_codes[status_code] += 1

            if line_count % 10 == 0:
                print_statistics(total_size, status_codes)

    except KeyboardInter
