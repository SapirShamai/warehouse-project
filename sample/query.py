from data import stock
from datetime import datetime
from collections import Counter

name = input("Please enter your name: ").capitalize()
print(f"Hallo, {name}!")
menu = """1. List items by warehouse
2. Search an item and place an order
3. Browse by category
4. Quit"""
number = int(input(f"What would you like to do: \n{menu}\nType the number of the operation: "))

if number == 1:
    print("\n### Warehouse 1 : ###\n")

    count_ware1 = 0
    for i in stock:
        items = i["state"] + " " + i["category"]
        if i["warehouse"] == 1:
            count_ware1 += 1
            print(items)

    print("\n### Warehouse 2 : ###\n")

    count_ware2 = 0
    for i in stock:
        items = i["state"] + " " + i["category"]
        if i["warehouse"] == 2:
            count_ware2 += 1
            print(items)

    print(f"\nTotal items in warehouse1: {count_ware1}")
    print(f"Total items in warehouse2: {count_ware2}\n")

    print(f"Thank you for your visit, {name}!")
    quit()


elif number == 2:
    x = 0
    while x == 0:
        item_name = input("What is the name of the item? ").lower()
        print(f"- {item_name}")
        amount = 0
        for item in stock:
            if (item["state"] + " " + item["category"]).lower() == item_name:
                amount += 1

        print(f"Total amount available: {amount}")
        amount1 = 0
        amount2 = 0

        print("Location: ")
        for item in stock:
            now = datetime.now()
            item_time = datetime.strptime(item["date_of_stock"], "%Y-%m-%d %H:%M:%S")

            if (item["state"] + " " + item["category"]).lower() == item_name and item["warehouse"] == 1:
                amount1 += 1
                print(f"-Warehouse 1 (in stock for {(now - item_time).days} days)")
            elif (item["state"] + " " + item["category"]).lower() == item_name and item["warehouse"] == 2:
                amount2 += 1
                print(f"-Warehouse 2 (in stock for {(now - item_time).days} days)")

        total_amount = amount1 + amount2
        if amount1 > amount2:
            print(f"Maximum availability {amount1} in Warehouse 1")
        elif amount1 == amount2 and amount1 != 0:
            print(f"The amount of items is the same in both warehouses: {amount1}")
        elif amount2 > amount1:
            print(f"Maximum availability {amount2} in Warehouse 2")
        else:
            answer = input(f"Not in stock\nWould you like to search for another item?  Y/N ").lower()
            if answer == "y" or answer == "yes":
                continue
            else:
                x += 1

        if total_amount > 0:
            answer = input(f"Would you like to place an order for {item_name}?  Y/N ").lower()
            if answer == "y" or answer == "yes":
                how_many = int(input(f"How many {item_name}s would you like? "))
                if 0 < how_many <= total_amount:
                    print(f"Your order: {how_many} {item_name} is placed!")
                    answer = input("Would you like to continue shopping?  Y/N ").lower()
                    if answer == "y" or answer == "yes":
                        continue
                    else:
                        x += 1
                else:
                    answer = input(
                        f"Error!\nThe maximus available is: {total_amount} items, would you like to take it instead?  Y/N ").lower()
                    if answer == "y" or answer == "yes":
                        print(f"Your order: {total_amount} {item_name} is placed!")
                        answer = input("Would you like to continue shopping?  Y/N ").lower()
                        if answer == "y" or answer == "yes":
                            continue
                        else:
                            x += 1
                    else:
                        x += 1
            else:
                x += 1


elif number == 3:
    my_category_list = []
    for i in stock:
        my_category_list.append(i["category"])
        categories = dict(Counter(my_category_list))
    for index, (key, value) in enumerate(categories.items()):
        print(f"{index + 1}. {key} ({value})")

    users_choice = int(input("Type the number of the category to browse: "))
    my_str_category = (list(categories)[users_choice - 1])
    print(f"List of {my_str_category} available:")
    for i in stock:
        if i["category"] == my_str_category:
            print("-", i["state"], i["category"] + ", Warehouse:", i["warehouse"])



elif number == 4:
    print(f"Thank you for your visit, {name}!")
    quit()

else:
    print(f"Error!\n{number} is an invalid operator, please try again.")

print(f"Thank you for your visit, {name}!")