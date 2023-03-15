from loader import Loader
from classes import *
from methods import *
stock = Loader(model="stock")   # dict with model and objects keys, objects= 4 warehouse objects
personnel = Loader(model="personnel")


user_history = []  # list with user actions

x = 0
while x == 0:
    user_name = get_name()   # Get the user_name

    guest = input("Would you like to continue as a guest? Y/N\n").lower()
    if guest == "y":
        user_name = User(user_name)  # -> greet user
        user_name.greet()
        x = 1
    else:
        password = input("Please enter your password:\n")
        my_emps = get_emp_name(personnel)  # -> return list with all employee objects
        match = 0
        for i in my_emps:   # -> to check which greet: employee or user
            if i._name == user_name and i.get_password() == password:
                user_name = Employee(user_name, password)
                user_name.greet()
                match = 1
                x = 1

        if not match:
            answer = input("User name or password is wrong, would you like to try again?\n").lower()
            if answer == "y":
                x = 0
            else:
                x = 1



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
        # if result:  # -> continue to order if there is such an item
        #
        #     user_history.append(f"Ordered {order_an_item(item_name, result, user_name)}")

    elif user_selection == 3:
        user_history.append(f"Browsed the category {browse_by_category()}")

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