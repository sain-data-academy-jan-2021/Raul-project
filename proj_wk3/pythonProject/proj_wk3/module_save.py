import csv
import fileinput
# saves changes to list / # function to use so we can save user input on file
def save_lists(fileName, list):
    with open(fileName, 'w') as list_file:
        list_file.writelines("%s\n" % line for line in list)

# saves changes to dictionary, saves user input to dic
def save_orders(data):
    with open('order.csv', 'w') as datafile:
        writer = csv.DictWriter(datafile, fieldnames = field_names)
        writer.writeheader()
        writer.writerows(data)
#save_orders(order)