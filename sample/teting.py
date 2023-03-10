from loader import Loader
from classes import *
from data import stock, personnel
from methods import *


user_history = []  # list with user actions

# user_name = User(get_name())   # Get the user_name
#
# print(greet_user(user_name._name))    # greet user

stock = Loader(model="stock")   # new data form:list with object for each warehouse
personnel = Loader(model="personnel")
ware1 = stock.objects[0]

# print(personnel.objects)
print(ware1.__dict__["stock"][0])








x = 0  # starting a loop that is keeping the user on the menu for as long as he wants
while x == 0:
    # Get the user selection(num) :
    user_selection = select_operator()

    # Execute operation:
    if user_selection == 1:           # list of each warehouse and the items in it plus total items in each warehouse
        list_of_items()
        user_history.append(f"Listed {list_of_items()} items")

    elif user_selection == 2:
        item_name = search_item()
        result = show_search_result(item_name, stock)
        user_history.append(f"Searched {item_name}")
        if result:

            user_history.append(f"Ordered {order_an_item(item_name, result, user_name)}")

    elif user_selection == 3:
        user_history.append(f"Browsed the category {browse_by_category(stock)}")

    elif user_selection == 4:
        pass

    else:
        print(f"Error!\n{user_selection} is an invalid operator, please try again.")

    more = input("Would you like to do anything else? Y/N\n").lower()
    if more == "y":
        x = 0
    else:
        x = 1

# end:

print(f"Thank you for your visit, {user_name}!\nIn this session you have:")
my_user_history(user_history)