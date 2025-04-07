# The script will find the lowest number in a file and write it to another file.
#
# Run as: python3 find_lowest_number.py <input_file> <output_file>
#
# Example: python3 find_lowest_number.py numbers.txt lowest_number.txt
#
# If python is setup to run as "python" instead of "python3" on the machine, 
# then we should use "python" instead of "python3" in the above.
#
# The input file should contain one number per line. The output file will 
# contain the lowest number.
#
# If the input file is blank, the output file will contain the text: "No 
# numbers found in file".

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
