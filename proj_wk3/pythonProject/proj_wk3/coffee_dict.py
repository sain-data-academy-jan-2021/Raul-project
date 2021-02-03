import module_save

def print_list(dictionary):
    for i, item in enumerate(dictionary):
        print(f" {i+1}. {item} - £{dictionary[item]:.2f}")


def get_details(chosen_coffee, chosen_size, chosen_extra):
    coffee = list(coffees)[chosen_coffee]
    price = coffees[coffee]
    size = list(sizes)[chosen_size]
    price += sizes[size]
    description = f"{size} {coffee}"
    if chosen_extra != 0:
        extra = list(extras)[chosen_extra]
        price += extras[extra]
        description += f" with {extra}"
    return description, price

# product dict and the key will have cofee and will have value in a list create an order dictionary
### coffes csv dict, size and extras in app, 
coffees = {"filter coffee": 1.5, "cappucino": 2.0, "latte": 2.1}
sizes = {"regular": 0.0, "large": 0.5, "bucket of": 1.0}
extras = {"nothing": 0.0, "an extra shot": 0.5, "syrup": 0.3, "sprinkles": 0.2}

while True:
    print("what type of coffee do you want?")
    print_list(coffees)
    coffee_id = int(input("choose a number from the list above ")) - 1
    print()

    print("what size do you want?")
    print_list(sizes)
    size_id = int(input("choose a number from the list above ")) - 1
    print()

    print("do you want anything with that?")
    print_list(extras)
    extra_id = int(input("choose a number from the list above ")) - 1
    print()

    drink_description, drink_price = get_details(coffee_id, size_id, extra_id)
    print(f"you have selected a {drink_description}")
    print(f"thanks, that will be £{drink_price:.2f}")
    print()

    print("do you want another coffee?")
    response = input(" (enter 'y' or 'yes' to continue) ")
    if not response.lower().startswith("y"):
        break
