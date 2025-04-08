
import sys

input_filename = sys.argv[1]
output_filename = sys.argv[2]

number_found = False

with open(input_filename, 'r') as input_file:
    for line in input_file:
        if number_found == False:
            try:
                lowest_number = int(line)
                number_found = True
            except ValueError:
                continue
        else:
            if int(line) < lowest_number:
                lowest_number = int(line)

with open(output_filename, 'w') as output_file:
    if number_found:
        output_file.write(str(lowest_number) + "\n")
    else:
        output_file.write("No numbers found in file\n")
