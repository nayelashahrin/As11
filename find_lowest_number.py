import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

lowest_number = None

with open(input_filename, 'r') as input_file:
    for line in input_file:
        # Remove any extra whitespace/newlines
        line = line.strip()
        # Skip empty lines
        if not line:
            continue
        try:
            number = float(line)
            # If it's the first valid number or if the current number is lower, update lowest_number.
            if lowest_number is None or number < lowest_number:
                lowest_number = number
        except ValueError:
            # Skip lines that cannot be converted to a number.
            continue

with open(output_filename, 'w') as output_file:
    if lowest_number is not None:
        output_file.write(str(lowest_number))
    else:
        output_file.write("No numbers found in file")
