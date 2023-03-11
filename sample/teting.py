from loader import Loader
from classes import *
from methods import *
stock = Loader(model="stock")   # dict with model and objects keys, objects= 4 warehouse objects
personnel = Loader(model="personnel")
# print(stock.__dict__)

#
# for employee in personnel:
#     print(employee._name)


user_history = []  # list with user actions

user_name = get_name()   # Get the user_name -> User object

print(greet_user(user_name._name))    # greet user

x = 0  # keeping the user on the menu for as long as he wants
while x == 0:
    # Get the user selection(num) :
    user_selection = select_operator()

    # Execute operation:
    if user_selection == 1:         # listing items by warehouse, users choice
        user_history.append(f"Listed {list_of_items()} items")  # adding to history

    elif user_selection == 2:
        item_name = get_name_of_item()
        show_search_result(item_name)
        # result = show_search_result(item_name, stock)
        user_history.append(f"Searched {item_name}")
        # if result:
        #
        #     user_history.append(f"Ordered {order_an_item(item_name, result, user_name)}")

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

print(f"Thank you for your visit, {user_name._name}!\nIn this session you have:")
my_user_history(user_history)