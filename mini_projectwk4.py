import os
import fileinput
import csv
import sys

import module_menus
import module_print
import module_read_data
import module_save
import module_add
from module_save import save_orders

ready_meal = module_read_data.read_from_file("ready_meal.txt")
courier = module_read_data.read_from_file("courier.txt")

order = []
product = []
courier = []

reader = csv.DictReader(open("product.csv"))
# Go through each line in csv file and add it to the list as dictionary (this is done by python automatically)
for row in reader:
    product.append(row)


reader = csv.DictReader(open("courier.csv"))
for row in reader:
    courier.append(row)

reader = csv.DictReader(open("order.csv"))
for row in reader:
    order.append(row)



def save_orders(data):
    with open('order.csv', 'w') as datafile:
        writer = csv.DictWriter(datafile, fieldnames=module_save.order_field_names)
        writer.writeheader()
        writer.writerows(data)


save_orders(order)

os.system("clear")


def delete_lists(filename, item):
    with open(filename, "r+") as f:
        d = f.readlines()
        f.seek(0)
        for i in d:
            if item not in i:
                f.write(i)
        f.truncate()


# def update_lists(filename, newitem):
#     with open(filename, "r+") as f:
#         data = f.readlines()
#         f.seek(0)
#         for item in data:
#             if item not in data:
#                 f.write(item)
#         f.write(newitem)

def update_data(filename, old, new):
    tmpFile = open(filename, 'r+')
    for line in fileinput.input(filename):
        if old in line:
            print("Match found")
            tmpFile.write(line.replace(old, new))
        else:
            tmpFile.write(line)
            print("No match found")
    tmpFile.close()


# define function to update meal use try and except to print out errors based on input
def update_object(existing_object, new_object, list):
    list.remove(existing_object)
    list.append(new_object)
    # print_object(list)


def start_program():
    choice_main_menu = module_menus.main_menu()
    while choice_main_menu != "0":
        if choice_main_menu == "1":
            os.system("clear")
            choice_product_menu = module_menus.product_menu()
            # used a while loop to go thru everything in product menu

            while choice_product_menu != "0":
                if choice_product_menu == "1":
                    os.system("clear")
                    # module_print.print_object(ready_meal)
                    module_print.print_data("product.csv")
                    # loopet backed at line 61 after we done everything in the if block 
                    choice_product_menu = module_menus.product_menu()

                elif choice_product_menu == "2":
                    os.system("clear")
                    new_product = input("What meal would you like to add? \n").title()
                    product_price = input("What is the price of the meal? \n").title()
                    if not new_product in product:
                        # use statment to ckeck if the item is already in the list


                        product.append(
                            {'Name': new_product, 'Price': product_price}
                        )

                        module_save.save_product(product)
                        # save_orders(order)

                        # module_add.add_new_object(new_product, ready_meal)
                        # module_save.save_lists("ready_meal.txt", ready_meal)
                    else:
                        print(f"{new_product} is already in the list")
                    new_product2 = input("Do you want to add another one? Yes or No \n").title()
                    os.system("clear")
                    if new_product2 != "No":
                        new_product3 = input("What meal would you like to add? \n").title()
                        new_product_price = input("What is the price of the meal? \n").title()
                        print("Your new meal is: " + new_product3 + " for " + new_product_price)

                        product.append(
                            {'Name': new_product, 'Price': product_price}
                        )

                        module_save.save_product(product)

                    # looped back to line 61 after checking everything in elif block
                    choice_product_menu = module_menus.product_menu()

                elif choice_product_menu == "3":
                    os.system("clear")
                    module_print.print_object(ready_meal)
                    product_to_update = input("What product would you like to update? \n").title()
                    if product_to_update not in ready_meal:
                        print(f"Product selected {product_to_update} does not exist")
                    else:
                        updated_product = input("What would you like to update this to? \n").title()
                        update_object(product_to_update, updated_product, ready_meal)
                        module_save.save_lists("ready_meal.txt", ready_meal)
                    # index_value = list.index(product_to_update)
                    choice_product_menu = module_menus.product_menu()
                elif choice_product_menu == "4":
                    os.system("clear")
                    # module_print.print_object(ready_meal)

                    module_print.print_data("product.csv")


                    module_add.delete_meal()


                    # module_add.delete_object(ready_meal)
                    module_save.save_lists("ready_meal.txt", ready_meal)
                    choice_product_menu = module_menus.product_menu()
                else:
                    os.system("clear")
                    print("Option selected is invalid")
                    choice_product_menu = module_menus.product_menu()
            os.system("clear")
            choice_main_menu = module_menus.main_menu()
        elif choice_main_menu == "2":
            os.system("clear")
            choice_courier_menu = module_menus.courier_menu()
            while choice_courier_menu != "0":
                if choice_courier_menu == "1":
                    os.system("clear")



                    module_print.print_data("courier.csv")
                    # loopet backed at line 61 after we done everything in the if block 
                    choice_courier_menu = module_menus.courier_menu()

                elif choice_courier_menu == "2":
                    os.system("clear")
                    new_courier = input("What name would you like to add? \n").title()
                    courier_phone = input("What is the phone number? \n").title()

                    courier.append(
                        {'Name': new_courier, 'Phone': courier_phone}
                    )

                    module_save.save_courier(courier)

                    choice_courier_menu = module_menus.courier_menu()
                elif choice_courier_menu == "3":
                    os.system("clear")
                    module_print.print_object(courier)
                    courier_to_update = input("What courier would you like to update? \n").title()
                    updated_courier = input("What would you like to update this to? \n").title()
                    update_object(courier_to_update, updated_courier, courier)
                    module_save.save_lists("courier.txt", courier)
                    choice_courier_menu = module_menus.courier_menu()
                elif choice_courier_menu == "4":
                    os.system("clear")
                    module_add.delete_object(courier)
                    module_save.save_lists("courier.txt", courier)
                    choice_courier_menu = module_menus.courier_menu()
                else:
                    os.system("clear")
                    print("Option selected is invalid")
                    choice_product_menu = module_menus.product_menu()
            os.system("clear")
            choice_main_menu = module_menus.main_menu()
        elif choice_main_menu == "3":
            os.system("clear")
            choice_order_menu = module_menus.order_menu()
            while choice_order_menu != "0":
                if choice_order_menu == "1":
                    module_print.print_data("order.csv")
                    # order_menu()
                    choice_order_menu = module_menus.order_menu()
                elif choice_order_menu == "2":
                    os.system("clear")
                    # add a key and a value in dictionary use cap input
                    name = input("Please enter the name of new order \n").title()
                    address = input("Please type the address for delivery \n").title()
                    phone = input("Please enter phone number \n").title()
                    delv_method = input("Please add the delivery method \n").title()
                    status = input("Please enter the status of the order \n").title()
                    #
                    product_choice_input = ""

                    # List for all the items user selected
                    product_selection = []


                    while product_choice_input != "0":
                        # prints all the items
                        module_print.print_data("product.csv")
                        # takes the input
                        product_choice_input = input("Select product from list below or type 0 to return \n").title()

                        if product_choice_input != 0:
                            # add the user input to the list of items as long as it's not zero
                            product_selection.append(product_choice_input)


                    # for order in orders:
                    #     if order['Name'] == "Order 1":
                    #         order['Statis'] = "Shipping"



                    # Needs an array for the product

                    order.append(
                        {'Name': name, 'Address': address, 'Phone': phone, 'Courier': delv_method, 'Status': status, 'Items': ','.join(product_selection)}
                    )
                    save_orders(order)
                    module_print.print_data("order.csv")
                    # Have to call save_lists to save it to the file
                    # add_new_object(name, courier)
                    # module_save.save_lists('courier.txt', courier)
                    # save_orders(order)
                    choice_order_menu = module_menus.order_menu()
                elif choice_order_menu == "3":
                    os.system("clear")
                    # print key and values from dictionary on different lines
                    module_print.read_orders()
                    # select key to delete from dictionary, use title for capitalize input
                    select_order = input("Please select a order to delete \n")
                    try:
                        # del order[index]
                        for index, item in enumerate(order):
                            if select_order in item.values():
                                del order[index]
                        save_orders(order)
                        delete_lists("courier.txt", select_order)
                        print(f" {select_order} has been removed from the list")
                        module_print.read_orders()
                        choice_order_menu = module_menus.order_menu()
                    except KeyError:
                        print(f"order selected {select_order} does not exist")
                        choice_order_menu = module_menus.order_menu()
                elif choice_order_menu == "4":
                    os.system("clear")
                else:
                    os.system("clear")
                    print("Option selected is invalid")
                    choice_order_menu = module_menus.order_menu()
            os.system("clear")
            choice_main_menu = module_menus.main_menu()
            #     os.system("clear")
        # choice_main_menu = main_menu()


start_program()
