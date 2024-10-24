#!/usr/bin/python3
import sys
import signal

"""
A script that parses logs line by line from stdin, computes the total file size
and the frequency of various HTTP status codes, and prints these metrics every
10 lines or upon receiving a keyboard interruption (CTRL + C).

Usage:
    The script reads from stdin and expects input in the format:
    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

    If a line does not follow this format, it is skipped.
    After every 10 lines and/or keyboard interruption, it prints:
    - Total file size
    - Number of occurrences of specific status codes (200, 301, 400, 401, 403, 404, 405, 500)
"""

# Initialize variables
total_size = 0
line_count = 0
status_counts = {
    200: 0,
    301: 0,
    400: 0,
    401: 0,
    403: 0,
    404: 0,
    405: 0,
    500: 0
}


def print_stats():
    """
    Prints the current total file size and counts for each status code.
    Only status codes with non-zero counts are printed.
    """
    print(f"File size: {total_size}")
    for code in sorted(status_counts.keys()):
        if status_counts[code] > 0:
            print(f"{code}: {status_counts[code]}")


def signal_handler(sig, frame):
    """
    Handles the keyboard interruption (CTRL + C) signal. Prints the current
    statistics (total file size and status code counts) before exiting the program.
    """
    print_stats()
    sys.exit(0)


# Set up signal handler for CTRL + C
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Skip the line if it does not have the correct format (at least 7 parts)
        if len(parts) < 7:
            continue

        # Extract status code and file size from the line
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            if status_code in status_counts:
                status_counts[status_code] += 1
            total_size += file_size

        except (ValueError, IndexError):
            # Ignore lines with invalid status codes or file sizes
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
