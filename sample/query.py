from data import stock, personnel
from datetime import datetime
from collections import Counter
from methods import get_name, greet_user, select_operator, list_of_items, search_item, show_search_result, order_an_item, browse_by_category

# Get the user_name:
user_name = get_name()

# greet user:
print(greet_user(user_name))

# Get the user selection(num) :
user_selection = select_operator()

# Execute operation:
if user_selection == 1:           # list of each warehouse and the items in it plus total items in each warehouse
    list_of_items()


elif user_selection == 2:
    item_name = search_item()
    result = show_search_result(item_name, stock)
    if result:
        order_an_item(item_name, result)

elif user_selection == 3:
    browse_by_category(stock)

elif user_selection == 4:
    pass

else:
    print(f"Error!\n{user_selection} is an invalid operator, please try again.")

# end:
print(f"Thank you for your visit, {user_name}!")