#!/usr/bin/python3

import sys
import signal

def print_stats(status_counts, total_size):
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
    print_stats(status_counts, total_size)
    sys.exit(0)

# Initialize variables
total_size = 0
line_count = 0
status_counts = {
    "200": 0,
    "301": 0,
    "400": 0,
    "401": 0,
    "403": 0,
    "404": 0,
    "405": 0,
    "500": 0
}

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
            status_code = parts[-2]  # status code
            file_size = int(parts[-1])  # file size
            
            if status_code in status_counts:
                status_counts[status_code] += 1
            total_size += file_size

        except (ValueError, IndexError):
            continue

        # Print stats every 10 lines
        if line_count % 10 == 0:
            print_stats(status_counts, total_size)

except KeyboardInterrupt:
    print_stats(status_counts, total_size)
    sys.exit(0)
