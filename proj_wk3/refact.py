
# Example 12*4+7/4
# Example 2 - ignore errorsperson = create_person(firstname, surname, age, city, nationality, gender, height, weight)
# Example 3 def get_lengthy_condition(data): return data is not None and data != "" and len(data) > 3 and len(data) < 20

a = 12*4+7/4

# takes person info and turns it into a dictionary
def create_person(firstname, surname, age, city, nationality, gender, height, weight):
    person = { "first_name":firstname, 
            "sur_name":surname, 
            "age":age,"city":city, 
            "nationality":nationality, 
            "gender":gender, 
            "height":height, 
            "weight":weight}
    return person 

# data must be a string, using if, else for len 
def get_lengthy_condition(data:str):
    if 3 < len(data) < 20 :
        return data
    else :
        return None

print(a)
print(create_person("firstname", "surname", "age", "city", "nationality", "gender", "height", "weight"))
print(get_lengthy_condition("data must be a"))
