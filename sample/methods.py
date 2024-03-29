from collections import Counter
from classes import *


# to get the name of the user:
def get_name():
    return input("Please enter your name: ").capitalize()


def create_user_object(user_name):
    """create user object with given username or anonymous, greet the user
    return user_name as a User object"""

    if user_name == "":
        user_name = User()
        user_name.greet()
        return user_name
    else:
        user_name = User(user_name)
        user_name.greet()
        return user_name


def get_employees_names(list_emp_obj):
    """takes a list with employee objects and returns a list with all employees names
     the list ia outside the func because it's recursive"""

    employee_names = []
    for employee in list_emp_obj:
        # print(employee._name) # -> gust to get the names, no list
        employee_names.append(employee)
        if employee.head_of:  # -> truthy
            employee_names += get_employees_names(employee.head_of)  # -> calling the func recursively + add to list
    return employee_names


def varify_employee(user_name, list_of_employees_names):
    """takes name and list of employees names, asking for password make sure it matches employee in list
        return the employee as an Employee object"""

    password = input("Please enter your password:\n")
    for employee in list_of_employees_names:
        if employee.is_named(user_name) and employee.authenticate(password):
            user_name = employee
            user_name.greet()  # -> greet employee
            return user_name
    return user_name


# to get number of operator from the menu:
def select_operator():
    """present the menu and ask for operation from user,check if number(doesn't check range), return int"""

    menu = """
    1. List items by warehouse
    2. Search an item and place an order
    3. Browse by category
    4. Quit
    """
    print(f"\nWhat would you like to do: \n{menu}")
    while True:
        answer = input(f"\nType the number of the operation:\n")
        if answer.isnumeric():
            return int(answer)
        else:
            print("Please enter a number.")


# print the list of items and how many in which warehouse:
def list_of_items(stock):
    """takes list with warehouse objects listing all the item return ware_id and total num of items """

    ware_id = input("Which warehouse would you like to view?\n")
    my_ware_ids = []
    for ware in stock:
        my_ware_ids.append(ware.warehouse_id)
    if ware_id in my_ware_ids:
        print(f"Items in warehouse {ware_id}:\n")
        for i in stock:
            if i.warehouse_id == ware_id:
                for item in i.stock:  # -> stock of ware object
                    print(item)
                print(f"\nTotal items in warehouse {i.warehouse_id}: {i.occupancy()}")
                return f"{i.occupancy()} items in warehouse {i.warehouse_id}"
    else:
        print("Error! this warehouse doesn't exist")


# search and order items:
def get_name_of_item():
    """ return the name of the chosen item """

    item_name = input("What is the name of the item?\n").lower()
    return item_name


def show_search_result(item_name, stock):
    """takes the name of the item that the user wants to search for
    returns the total amount"""

    total_amount = 0
    for ware in stock.objects:  # -> warehouse object
        my_list_items = ware.search_item(item_name)  # -> list of matches
        if not my_list_items:  # -> falsy
            print("We couldn't find this item in our warehouses")
            break
        else:
            print(f"Warehouse {ware.warehouse_id} total amount: {len(my_list_items)}")
            total_amount += len(my_list_items)
    print(f"Total amount: {total_amount}")
    return total_amount


# order functions (only for employee):

def want_to_order(item_name, stock):
    """check if user interested in placing an order and if the warehouse exists in the stock wares"""

    order = input(f"Would you like to place an order for {item_name}?  Y/N \n").lower()
    ware_id = input("From which warehouse would you like to place your order?\n")
    if order == "y":
        my_ware_ids = []
        for ware in stock:
            my_ware_ids.append(ware.warehouse_id)
        if ware_id in my_ware_ids:
            return ware_id
        else:
            print("Error! this warehouse is not exist")
            return False


def show_available_to_order(item_name, warehouse_id, stock):
    """list the items in a specific warehouse, return list of matching items by ware """

    for ware in stock:
        if ware.warehouse_id == warehouse_id:
            my_list_items = ware.search_item(item_name)  # -> list of matches from specific ware
            print(f"****** Total amount in warehouse{warehouse_id}: {len(my_list_items)} *******\nDescription:\n")

            now = datetime.now()  # print the items and how long in stock
            for i in my_list_items:
                item_time = datetime.strptime(i.date_of_stock, "%Y-%m-%d %H:%M:%S")
                print(f"{i} in warehouse: {i.warehouse}, {(now - item_time).days} days in stock")
            return my_list_items


def order_an_item(user_name, item_name, list_of_matches_in_ware):
    """order the item and check right quantity"""

    item_amount = int(input(f"\nHow many {item_name}s would you like to order?\n"))
    if 0 < item_amount <= len(list_of_matches_in_ware):   # check if amount in ware
        user_name.order(item_name, item_amount)
        return True
    else:
        print("Error! this amount is not available")
        answer = input(f"Maximum amount is {len(list_of_matches_in_ware)}, would you like to place order? Y/N\n").lower()
        if answer == "y":
            user_name.order(item_name, len(list_of_matches_in_ware))
            return True
    return False


# categories functions:
def create_categories(stock):
    """print list to user with categories and amount from each category
    return dict with this info"""

    print("****** Categories ******\n")
    my_category_list = []
    for ware in stock:
        for i in ware.stock:
            my_category_list.append(i.category)
    categories = dict(Counter(my_category_list))
    for index, (key, value) in enumerate(categories.items()):
        print(f"{index + 1}. {key} ({value})")
    return categories


def browse_by_category(categories_dict, stock):
    """takes dict convert it to a list of keys, browse items full name and location by category.
    return the name of the category that has been browsed"""

    users_choice = int(input("\nType the number of the category to browse: "))
    my_str_category = (list(categories_dict)[users_choice - 1])  # -> list with only the keys
    print(f"\nList of {my_str_category} available:")
    for ware in stock:  # -> loop ware objects
        for i in ware.stock:  # -> loop item objects in each ware
            if i.category == my_str_category:
                print(f"- {i.state} {i.category}, Warehouse: {i.warehouse}")

    return my_str_category
