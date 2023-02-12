from data import stock, personnel
from datetime import datetime
from collections import Counter
from methods import get_name, greet_user, select_operator, list_of_items, search_and_order_item, browse_by_category

# Get the user name and greet:
user_name = get_name()
print(greet_user(user_name))

# get the number for selection from user:
user_selection = select_operator()

# Execute operation:
if user_selection == 1:
    print(list_of_items())

elif user_selection == 2:
    #print(search_item())
    print(search_and_order_item())

elif user_selection == 3:
    print(browse_by_category(stock))

elif user_selection == 4:
    pass

else:
    print(f"Error!\n{user_selection} is an invalid operator, please try again.")

# end:
print(f"Thank you for your visit, {user_name}!")