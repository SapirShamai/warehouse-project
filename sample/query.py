from methods import *

stock = Loader(model="stock")  # dict with model and objects keys, objects= 4 warehouse objects
personnel = Loader(model="personnel")

while True:
    user_name = get_name()  # Get the user_name
    guest = input("Would you like to continue as a guest? Y/N\n").lower()

    if guest == "y":
        user_name = User(user_name)  # -> greet user
        user_name.greet()
        break
    else:
        password = input("Please enter your password:\n")
        my_emps = get_emp_name(personnel)  # -> return list with all employee objects
        match = 0
        for employee in my_emps:
            if employee.is_named(user_name) and employee.authenticate(password):
                user_name = employee
                user_name.greet()  # -> greet employee
                match = 1

        if match:
            break
        else:
            answer = input("User name or password is wrong, would you like to try again?\n").lower()
            if answer == "y":
                continue
            else:
                break

while True:

    user_selection = select_operator()  # Get the user selection(num)

    if user_selection == 1:  # listing items by warehouse
        Employee.list_of_actions.append(f"Listed {list_of_items()} items")  # adding to history
        # I'm adding to history anyway, return the history only if user is employee

    elif user_selection == 2:
        # search part:
        item_name = get_name_of_item()
        search_result = show_search_result(item_name)
        Employee.list_of_actions.append(f"Searched {item_name}")
        # order part:
        if type(user_name) is Employee and search_result > 0:  # -> continue to order if there is such an item
            ware_id = want_to_order(item_name)
            if int(ware_id) > 0:
                list_matching_items_by_ware = show_available_to_order(item_name, ware_id)
                my_order = order_an_item(item_name, list_matching_items_by_ware)
                if my_order:    # -> only if order has been placed add to history
                    Employee.list_of_actions.append(f"Ordered {item_name}")

    elif user_selection == 3:
        Employee.list_of_actions.append(f"Browsed the category {browse_by_category()}")

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
