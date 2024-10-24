#!/usr/bin/python3
import sys
import signal

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

# Function to print statistics
def print_stats():
    print(f"File size: {total_size}")
    for status_code in sorted(status_counts.keys()):
        if status_counts[status_code] > 0:
            print(f"{status_code}: {status_counts[status_code]}")

# Signal handler for keyboard interruption (CTRL + C)
def signal_handler(sig, frame):
    print_stats()
    sys.exit(0)

# Set up signal handling
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
