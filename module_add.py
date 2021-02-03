import os
import fileinput

from tabulate import tabulate

import module_print
import pandas as pd
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


def delete_meal():
    # Take the item
    item = input("What would you like to delete? \n").title()
    # Read the existing file
    df = pd.read_csv("product.csv")
    # New dataframe where the item isn't included
    new_df = df[df.Name != item]
    # Rewrite the file with new dataframe
    new_df.to_csv("product.csv", index=False)



