from loader import Loader
from classes import *
from methods import *
stock = Loader(model="stock")   # dict with model and objects keys, objects= 4 warehouse objects
personnel = Loader(model="personnel")
# print(stock.__dict__)

for employee in personnel:
    print(employee._name)
print(len(list(stock))) # amount of warehouses

user_history = []  # list with user actions

user_name = User(get_name())   # Get the user_name

print(greet_user(user_name._name))    # greet user

x = 0  # keeping the user on the menu for as long as he wants
while x == 0:
    # Get the user selection(num) :
    user_selection = select_operator()

    # Execute operation:
    if user_selection == 1:           # list of each warehouse and the items in it plus total items in each warehouse
        list_of_items()
        # user_history.append(f"Listed {list_of_items()} items")

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