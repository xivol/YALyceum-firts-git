# This is a sample Python script.
import sys
import csv

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'DUPER, {name}')
    print(f'Hi, {name}')
    print(f'Hi, {name}')
    print(f'Hi, {name}')
    print(f'Hi, {name}')
    print(f'Hi, {name}')
    print(f'Hi, {name}')
    print(f'Hi, {name}')

    # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/


title = "nomen, definitio, pluma, Russian nomen,\
 familia, Russian nomen familia".split(", ")

lines = sys.stdin.readlines()

csvfile = open('plantis.csv', 'w', newline='')
writer = csv.writer(csvfile, delimiter=';', quotechar='"',
                    quoting=csv.QUOTE_MINIMAL)

writer.writerow(title)
for line in lines:
    writer.writerow(line.strip().split('\t'))

csvfile.close()