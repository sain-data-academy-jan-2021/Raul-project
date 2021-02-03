import csv
import fileinput
# saves changes to list / # function to use so we can save user input on file

order_field_names = ['Name', 'Address', 'Phone', 'Courier', 'Status', 'Items']
courier_field_names = ['Name', 'Phone']
product_field_names = ['Name', 'Price']


def save_lists(fileName, list):
    with open(fileName, 'w') as list_file:
        list_file.writelines("%s\n" % line for line in list)

# saves changes to dictionary, saves user input to dic
def save_orders(data):
    # Open the csv file
    with open('order.csv', 'w') as datafile:
        # Set the fieldnames and add the passed "data" to the file
        writer = csv.DictWriter(datafile, fieldnames = order_field_names)
        writer.writeheader()
        writer.writerows(data)
#save_orders(order)

def save_courier(data):
    with open('courier.csv', 'w') as datafile:
        writer = csv.DictWriter(datafile, fieldnames=courier_field_names)
        writer.writeheader()
        writer.writerows(data)

def save_product(data):
    with open('product.csv', 'w') as datafile:
        writer = csv.DictWriter(datafile, fieldnames=product_field_names)
        writer.writeheader()
        writer.writerows(data)
