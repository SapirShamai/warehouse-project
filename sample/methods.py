from collections import Counter
from loader import Loader
from classes import *
stock = Loader(model="stock")   # dict with model and objects keys, objects= 4 warehouse objects
personnel = Loader(model="personnel")

# to get the name of the user:
def get_name():
    return input("Please enter your name: ").capitalize()


# to greet the user:
def greet_user(name):
    return (f"Hallo, {name}!")

# to get number of operator from the menu:
def select_operator():
    menu = """
    1. List items by warehouse
    2. Search an item and place an order
    3. Browse by category
    4. Quit
    """
    return int(input(f"What would you like to do: \n{menu}\nType the number of the operation: "))


# print the list of items and how many in which warehouse:
def list_of_items():
    ware_num = int(input("Which warehouse would you like to view?\n"))
    my_warehouses = []
    for i in stock:   # items are 4 warehouse objects
        my_warehouses.append(i.warehouse_id)
    if str(ware_num) in my_warehouses:
        print(f"Items in warehouse {ware_num}:\n")
        for i in stock:
            if i.warehouse_id == str(ware_num):
                for item in i.stock:
                    print(item)
                print(f"len(i.stock))
                return len(i.stock)
    else:
        print("Error! this warehouse is out of range")


# search and order items:
def search_item():
    ''' return the name of the chosen item '''                   # get the item name

    item_name = input("What is the name of the item? ").lower()
    return item_name


def show_search_result(item_name, stock):                          # search item in stock
    '''
    print the search result:
    total amount of item (from search_item()) in stock,
    on which warehouse, how long in stock, max availability
    '''
    x = 0
    while x == 0:
        amount = 0
        for item in stock:
            if (item["state"] + " " + item["category"]).lower() == item_name:
                amount += 1
        print(f"Total amount available: {amount}")

        print("Location: ")
        warehouses = {}
        for item in stock:
            key = item["warehouse"]
            now = datetime.now()
            item_time = datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S")
            time_in_stock = str((now - item_time).days)
            if (item["state"] + " " + item["category"]).lower() == item_name:
                print("Warehouse " + str(item["warehouse"]) + ": " + time_in_stock + " days in stock")
                if key not in warehouses.keys():
                    warehouses[key] = 1
                else:
                    warehouses[key] += 1
        for key, value in warehouses.items():
            print(f"-Total amount in Warehouse {key}: {value} items")

        if warehouses:
            my_max = max(warehouses.items(), key=lambda x:x[1])
            print(f"\nMaximum availability {my_max[1]} in Warehouse {my_max[0]}")
            x = 1

        elif not warehouses:
            answer = input(f"{item_name} is not in stock, would you like to search for a different item? ").lower()
            if answer == "y":
                item_name = search_item()
                x = 0
            else:
                x = 1
    return warehouses


# order the item:
def order_an_item(item_name, warehouses, user_name):
    '''
    this function is taking item and dict with keys(warehouse) and values(amount available)
    returning the item name and the number of the items that the user ordered
    or None if order has not been placed
    '''
    order = input(f"Would you like to place an order for {item_name}?  Y/N \n").lower()
    if order == "y" or order == "yes":                             # if the user wants to order he should be registered
        password = input("Enter your password:\n").lower()

        if name_and_password(personnel, user_name, password):
            print("You are authorized!")
            key = int(input("From which warehouse would you like to place your order?\n"))
            if key in warehouses:
                my_max_amount = warehouses[key]                          # to get the value from the key chosen by th user
                amount_by_user = int(input(f"How many {item_name}s would you like from Warehouse {key} ?\n"))
                if 0 < amount_by_user <= my_max_amount:
                    print(f"Your order: {amount_by_user} {item_name}s from warehouse {key} is placed!")
                    return str(amount_by_user) + " " + item_name
                    # would you like to order anything else?

                else:
                    different_amount = input(f"Error!\nThe maximus available is: {my_max_amount} items in Warehouse {key}, would you like to take it instead?  Y/N\n").lower()
                    if different_amount == "y" or order == "yes":
                        print(f"Your order: {my_max_amount} {item_name}s from warehouse {key} is placed!")
                        return my_max_amount, item_name
                    # would you like to order anything else?

            else:
                print("this item does not exist in this warehouse")
                return None
                # would you like to check in a different warehouse?
        else:
            print("User is not in th system.")

# browse items by category:
def browse_by_category(stock):
    '''
    listing the categories, browse items full name and location by category.
    return the name of the category that has benn browsed
    '''
    my_category_list = []
    for i in stock:
        my_category_list.append(i["category"])
    categories = dict(Counter(my_category_list))
    for index, (key, value) in enumerate(categories.items()):
        print(f"{index + 1}. {key} ({value})")

    users_choice = int(input("\nType the number of the category to browse: "))       # to get the number
    my_str_category = (list(categories)[users_choice - 1])                         # the item name
    print(f"\nList of {my_str_category} available:")
    for i in stock:
        if i["category"] == my_str_category:
            x = ("- " + i["state"] + " " + i["category"] + ", Warehouse: " + str(i["warehouse"]))
            print(x)

    return my_str_category


def my_user_history(*user_history):
    '''
    this function takes a list of users actions and returns then numbered one by one
    '''
    for index, action in enumerate(*user_history):
        print(index + 1, ".", action)


# functions for the user system

def pars_users(my_dict_list, my_list):
    for item in my_dict_list:
        my_dict = {}
        my_dict["user_name"] = item["user_name"]
        my_dict["password"] = item["password"]
        my_list.append(my_dict)
        if "head_of" in item:
            pars_users(item["head_of"], my_list)


def name_and_password(personnel, user_name, password):
    my_employees_list = []
    for user in personnel:
        my_dict = {}
        my_dict["user_name"] = user["user_name"]
        my_dict["password"] = user["password"]
        my_employees_list.append(my_dict)
        if "head_of" in user:
            pars_users(user["head_of"], my_employees_list)
    for user in my_employees_list:
        if user["user_name"] == user_name and user["password"] == password:
            return True
    return False


# testing:
#name_and_password(personnel, "Lidia", "parker")

