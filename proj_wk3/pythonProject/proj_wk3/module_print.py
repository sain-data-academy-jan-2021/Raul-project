import csv
# print from list function
def print_object(list):
    for item in list:
        print("We have available " + item)

# print/reads from dictionary        
def read_orders():
    orderdata = csv.DictReader(open("order.csv"))
    print("Current Orders: \n")
    for row in orderdata:
        print(row)
