import random
import argparse

def get_random_lines(file_path, n):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        random_lines = random.sample(lines, n)
    return random_lines

def get_lines_from_start_to_end(file_path, start, end):
    with open(file_path, 'r') as file:
        lines = file.readlines()
        selected_lines = lines[start:end]
    return selected_lines

def save_lines_to_file(lines, output_file):
    with open(output_file, 'w') as file:
        for line in lines:
            file.write(line)

if __name__ == "__main__":
    parser = argparse.ArgumentParser()
    parser.add_argument("--start", type=int, help="Choose the start line")
    parser.add_argument("--end", type=int, help="Choose the end line")
    parser.add_argument("--type", type=int, default=1, help="Type = 0 for not random | Type = 1 for random | Default = random")
    parser.add_argument("-n", "--nr", type=int, help="Number of lines to generate")
    parser.add_argument("--output_file", help="Output file name", default="benign_new_gen.txt")
    args = parser.parse_args()

    n = args.nr
    type = args.type
    start = args.start
    end = args.end
    input_file_path = 'benign.txt'
    output_file_path = args.output_file

    if type == 1:
        random_lines = get_random_lines(input_file_path, n)
        save_lines_to_file(random_lines, output_file_path)
    elif type == 0:
        selected_lines = get_lines_from_start_to_end(input_file_path, start, end)
        save_lines_to_file(selected_lines, output_file_path)
