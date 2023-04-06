from collections import Counter
from loader import Loader
from classes import *

stock = Loader(model="stock")  # dict with model and objects keys, objects= 4 warehouse objects
personnel = Loader(model="personnel")


# to get the name of the user:
def get_name():
    return input("Please enter your name: ").capitalize()


def get_emp_name(list_emp_obj):
    '''
     takes a list with employee objects and returns a list with all employees names
     the list ia outside the func because it's recursive
    '''
    employee_names = []
    for employee in list_emp_obj:
        # print(employee._name) # -> gust to get the names, no list
        employee_names.append(employee)
        if employee.head_of:  # -> truthy
            employee_names += get_emp_name(employee.head_of)  # -> calling the func recursively adding the names to list
    return employee_names


# to get number of operator from the menu:
def select_operator():
    menu = """
    1. List items by warehouse
    2. Search an item and place an order
    3. Browse by category
    4. Quit
    """
    return int(input(f"\nWhat would you like to do: \n{menu}\nType the number of the operation:\n"))


# print the list of items and how many in which warehouse:
def list_of_items():
    ware_num = input("Which warehouse would you like to view?\n")
    my_warehouses = []
    for i in stock:  # items are 4 warehouse objects, in each there is ware_id and stock
        my_warehouses.append(i.warehouse_id)
    if ware_num in my_warehouses:
        print(f"Items in warehouse {ware_num}:\n")
        for i in stock:  # -> stock of ware object
            if i.warehouse_id == ware_num:
                for item in i.stock:
                    print(item)
                print(f"\nTotal items in warehouse {ware_num}: {i.occupancy()}")
                return i.occupancy()
    else:
        print("Error! this warehouse is out of range")


# search and order items:
def get_name_of_item():
    ''' return the name of the chosen item '''

    item_name = input("What is the name of the item?\n").lower()
    return item_name


def show_search_result(item_name):
    '''
    takes the name of the item that the user wants to search for
    returns the total amount
    '''

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

def want_to_order(item_name):
    """check if user interested in placing an order"""

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


def show_available_to_order(item_name, warehouse_id):
    """list the items in a specific warehouse, return list of matching items by ware """
    for ware in stock:
        if ware.warehouse_id == warehouse_id:
            my_list_items = ware.search_item(item_name)  # -> list of matches from specific ware
            print(f"Total amount in warehouse{warehouse_id}: {len(my_list_items)}")

            now = datetime.now()  # print the items and how long in stock
            for i in my_list_items:
                item_time = datetime.strptime(i.date_of_stock, "%Y-%m-%d %H:%M:%S")
                print(f"{i} in warehouse: {i.warehouse}, {(now - item_time).days} days in stock")
            return my_list_items


def order_an_item(item_name, list_of_matches_in_ware):
    """order the item and check right quantity"""
    item_amount = int(input(f"How many {item_name}s would you like to order?\n"))
    if 0 < item_amount <= len(list_of_matches_in_ware):
        print("Your order has been placed !")
        return True
    else:
        print("Error! this amount is not available")
        answer = input(f"Maximum amount is {len(list_of_matches_in_ware)}, would you like to place order? Y/N\n").lower()
        if answer == "y":
            print("Your order has been placed !")
            return True
    return False


def browse_by_category():
    '''
    listing the categories, browse items full name and location by category.
    return the name of the category that has benn browsed
    '''

    print("****** Categories ******\n")
    my_category_list = []
    for ware in stock:
        for i in ware.stock:
            my_category_list.append(i.category)
    categories = dict(Counter(my_category_list))
    for index, (key, value) in enumerate(categories.items()):
        print(f"{index + 1}. {key} ({value})")

    users_choice = int(input("\nType the number of the category to browse: "))  # to get the number
    my_str_category = (list(categories)[users_choice - 1])  # the item name
    print(f"\nList of {my_str_category} available:")
    for ware in stock:  # -> loop ware objects
        for i in ware.stock:  # -> loop item objects in each ware
            if i.category == my_str_category:
                print(f"- {i.state} {i.category}, Warehouse: {i.warehouse}")

    return my_str_category
