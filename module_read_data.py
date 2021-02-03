def read_from_file(fileName):
    with open(fileName, "r") as fileholder:
        info = fileholder.read().splitlines()
        return info
    
# def read_orders():
#     orderdata = csv.DictReader(open("order.csv"))
#     print("Current Orders: \n")
#     for row in orderdata:
#         print(row)
