import csv
import pandas as pd
from tabulate import tabulate


def print_object(list):
    for item in list:
        print("We have available " + item)

def print_data(file):
    df = pd.read_csv(file)
    # Tabulate pretty(formatted) prints the csv file
    print(tabulate(df, headers='keys', tablefmt='psql', showindex='never'))
