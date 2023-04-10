from methods import *
from loader import Loader
# data:
stock = Loader(model="stock")  # dict with model and objects keys, objects= 4 warehouse objects
personnel = Loader(model="personnel")

# user part:
while True:
    user_name = get_name()  # Get the user_name
    guest = input("Would you like to continue as a guest? Y/N\n").lower()

    if guest == "y":
        user_name = create_user_object(user_name)  # -> create and greet the User
        break
    else:
        my_employees = get_employees_names(personnel)   # -> return list with all employee objects
        user_name = varify_employee(user_name, my_employees)  # -> return user as employee object
        if isinstance(user_name, Employee):
            break
        else:
            answer = input("User name or password is wrong, would you like to try again? Y/N\n").lower()
            if answer == "y":
                continue
            else:
                user_name = create_user_object(user_name)  # -> create and greet the User
                break


# actions in warehouse:
while True:

    user_selection = select_operator()  # Get the user selection(num)

    if user_selection == 1:  # listing items by warehouse
        Employee.list_of_actions.append(f"Listed {list_of_items(stock)} ")  # adding to history anyway

    elif user_selection == 2:
        # search part:
        item_name = get_name_of_item()
        search_result = show_search_result(item_name, stock)
        Employee.list_of_actions.append(f"Searched {item_name}")
        # order part:
        if type(user_name) is Employee and search_result > 0:  # -> continue to order if there is such an item
            ware_id = want_to_order(item_name, stock)
            if int(ware_id) > 0:
                list_matching_items_by_ware = show_available_to_order(item_name, ware_id, stock)
                my_order = order_an_item(user_name, item_name, list_matching_items_by_ware)
                if my_order:    # -> only if order has been placed add to history
                    Employee.list_of_actions.append(f"Ordered {item_name}")

    elif user_selection == 3:
        my_categories = create_categories(stock)
        Employee.list_of_actions.append(f"Browsed the category {browse_by_category(my_categories, stock)}")

    elif user_selection == 4:
        break

    else:
        print(f"Error!\n{user_selection} is an invalid operator, please try again.")

    more = input("Would you like to do anything else? Y/N\n").lower()
    if more == "y":
        continue
    else:
        break

# end:

if type(user_name) is Employee:
    user_name.bye()
else:
    user_name.bye()
