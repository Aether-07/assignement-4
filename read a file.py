#Task 1
filename = input('Enter a filename: ')
try:
    file = open(filename, 'r')
    reading_file = file.read()
    file.close()
    print(reading_file)
except FileNotFoundError:
    print('the file does not exist')

#Task 2
enter_the_filename = input('Enter a filename: ')
try:
    write_data = input(f'Enter text to write to the file: {enter_the_filename}:')
    file1 = open(enter_the_filename, 'w')
    writing_file = file1.write(write_data)
    file1.close()
finally:
    print(f'Data successfully written to {enter_the_filename}:')
try:
    additional_data = input('Enter additional text to append:')
    file1 = open(enter_the_filename, 'a')
    appending_file1 = file1.write(additional_data)
    file1.close()
finally:
    print('Data successfully appended')

file1 = open(enter_the_filename,'r')
reading_file = file1.read()
file1.close()
print(f'Final content of {enter_the_filename}',reading_file)
