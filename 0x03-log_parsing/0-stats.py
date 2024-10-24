#!/usr/bin/python3
import sys
import signal

"""
A script that reads from stdin line by line and computes statistics on
log data following the format:

    <IP Address> - [<date>] "GET /projects/260 HTTP/1.1" <status code> <file size>

It prints statistics every 10 lines or upon receiving a keyboard interruption (CTRL + C),
showing the total file size and counts of specific status codes.

Usage:
    The script reads input via stdin and expects a log format as described above.
    If the format is invalid, the line is skipped.

Statistics Printed:
    - Total file size: sum of all file sizes from valid lines
    - Count of each valid status code (200, 301, 400, 401, 403, 404, 405, 500)
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
    Prints the total file size and counts of valid status codes (200, 301, 400, 401,
    403, 404, 405, 500). Only status codes with non-zero counts are printed.
    """
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")


def signal_handler(sig, frame):
    """
    Handles the keyboard interruption (CTRL + C) signal. Prints the current
    statistics (total file size and status code counts) before exiting the program.

    Args:
        sig (int): Signal number.
        frame (FrameType): Current stack frame (ignored in this case).
    """
    print_stats()
    sys.exit(0)


# Set up signal handling for keyboard interruption
signal.signal(signal.SIGINT, signal_handler)

try:
    for line in sys.stdin:
        line_count += 1
        parts = line.split()

        # Skip line if the format is not correct
        if len(parts) < 7:
            continue

        # Extract file size and status code
        try:
            status_code = int(parts[-2])
            file_size = int(parts[-1])

            if status_code in status_counts:
                status_counts[status_code] += 1
            total_size += file_size

        except (ValueError, IndexError):
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats()

except KeyboardInterrupt:
    print_stats()
    sys.exit(0)
