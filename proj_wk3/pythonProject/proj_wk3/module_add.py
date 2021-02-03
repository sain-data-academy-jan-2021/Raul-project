import os
import fileinput
import module_print
def add_new_object(item, list):
    list.append(item)
    module_print.print_object(list)
    
def delete_object(list):
    item = input("What would you like to delete? \n").title()
    if item in list:
        list.remove(item)
        os.system("clear")
        print(f" {item} has been removed from the list")
        module_print.print_object(list)
    elif item not in list:
        print(f"Product selected {item} does not exist")