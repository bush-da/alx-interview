#!/usr/bin/python3

import sys
import signal


def print_stats(dict_sc, total_file_size):
    """
    Prints the total file size and counts for each status code.

    Args:
        dict_sc: Dictionary of status codes with their counts.
        total_file_size: Total file size from processed lines.
    """
    print("File size: {}".format(total_file_size))
    for key, val in sorted(dict_sc.items()):
        if val != 0:
            print("{}: {}".format(key, val))


def signal_handler(sig, frame):
    """
    Handles keyboard interruption (CTRL + C) by printing current stats
    before exiting the program.
    """
    print_stats(dict_sc, total_file_size)
    sys.exit(0)


# Initialize variables
total_file_size = 0
counter = 0
dict_sc = {
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
        parsed_line = line.split()  # Split the line into components
        counter += 1

        if len(parsed_line) >= 7:  # Check if line has enough components
            try:
                file_size = int(parsed_line[-1])  # Get file size
                status_code = parsed_line[-2]  # Get status code

                total_file_size += file_size  # Update total file size

                if status_code in dict_sc:  # Update status code count
                    dict_sc[status_code] += 1

            except (ValueError, IndexError):
                continue  # Skip lines with invalid data

            if counter == 10:  # Print stats every 10 lines
                print_stats(dict_sc, total_file_size)
                counter = 0  # Reset counter after printing

finally:
    print_stats(dict_sc, total_file_size)  # Print final stats on exit
