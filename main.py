import random

# user inputs
name = input("Enter your name: ")
surname = input("Enter your surname: ")
number = (input("Enter your number: "))


# creating lists from inputs
def name_fun(name_):
    return [n for n in name_]


def surname_fun(surname_):
    return [s for s in surname_]


def number_fun(number_):
    return [s for s in number_]


# assigning the lists to variables
name_list = name_fun(name)
surname_list = surname_fun(surname)
number_list = number_fun(number)
special_characters = ["$", "!", "@", "#", "%"]

# choosing random letters from the above lists
from_name = random.sample(name_list, 3)
from_surname = random.sample(surname_list, 2)
from_number = random.sample(number_list, 2)
from_special = random.sample(special_characters, 1)

# creating th password list
password_list = from_name + from_number + from_surname + from_special


# converting the list into a string
def toString(password_array):
    return "".join(password_array).capitalize()


print("\nHere is your password: ")
print("\t" + toString(password_list))
