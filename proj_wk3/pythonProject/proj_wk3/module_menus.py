def main_menu():
    user_choice =  input(""" 

••• Welcome to PY Cafe ••• 
___________________________
|•1• Enter Products Menu  |
|•2• Enter Courier Menu   |
|•3• Enter Orders         |
|•4• Exit App             |
---------------------------
Please Make a Selection
""")
# returns/saves user input to be used later on
    return user_choice

def product_menu(): 
    user_choice = input ("""

•••••• Shopping Basket ••••••  
_____________________________
|•1• View Ready Meals-Lunche|
|•2• Add a Meal to Basket   |
|•3• Update Meal from Basket|
|•4• Remove Meal from Basket|
|•0• Return to Main Menu    |
-----------------------------
Please Make a Selection
""")
    return user_choice

def courier_menu(): 
    user_choice = input ("""

•••••• Shopping Basket ••••••  
_____________________________
|•1• View All Couriers      |
|•2• Add a Courier          |
|•3• Update a Courier       |
|•4• Remove a Courier       |
|•0• Return to Main Menu    |
-----------------------------
Please Make a Selection
""")
    return user_choice
# takes user input and saves it in a variable

def order_menu():
    user_choice =  input(""" 

•••   Order Menu   ••• 
_____________________
|•1• View Orders    |
|•2• Add Order      |
|•3• Delete Order   |
|•4• Update Status  |
|•0• Exit App       |
---------------------
Please Make a Selection
""")
    return user_choice
