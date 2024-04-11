import os
import re
import datetime
import time


def find_serial_numbers(root_dir):
    serial_number_pattern = r'N\w{3}-\d{5}'
    serial_numbers = []

    for root, dirs, files in os.walk(root_dir):
        for file in files:
            file_path = os.path.join(root, file)
            with open(file_path, 'r') as f:
                content = f.read()
                matches = re.findall(serial_number_pattern, content)
                for match in matches:
                    serial_numbers.append((file, match))

    return serial_numbers


def format_table(serial_numbers, search_date, search_duration):
    table = '-' * 50 + '\n'
    table += f'Search date: {search_date}\n\n'
    table += 'FILE\t\tSERIAL NO.\n'
    table += '----\t\t----------\n'
    for file, serial in serial_numbers:
        table += f'{file}\t{serial}\n'
    table += '\nNumbers found: {}\n'.format(len(serial_numbers))
    table += 'Search duration: {} seconds\n'.format(round(search_duration))
    table += '-' * 50 + '\n'
    return table


def main(root_dir):
    start_time = time.time()
    serial_numbers = find_serial_numbers(root_dir)
    end_time = time.time()
    search_date = datetime.datetime.now().strftime('%d/%m/%Y')
    search_duration = end_time - start_time
    table = format_table(serial_numbers, search_date, search_duration)
    print(table)


if __name__ == "__main__":
    root_dir = 'My_Big_Directory'  # Specify the root directory here
    main(root_dir)
