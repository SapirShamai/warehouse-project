from data import warehouse1, warehouse2

name = input("Please enter your name: ")
print(f"Hallo, {name.capitalize()}!")
menu = """1. List items by warehouse
2. Search an item and place an order
3. Quit"""
number = int(input(f"What would you like to do: \n{menu}\nType the number of the operation: "))

if number == 1:
    print("### Warehouse1 Items ###")
    for item in warehouse1:
        print(item)

    print("### Warehouse2 Items ###")
    for item in warehouse2:
        print(item)

    print(f"Thank you for your visit, {name}!")
    quit()


elif number == 2:
    x = 0
    while x == 0:
        item_name = input("What is the name of the item? ")
        amount1 = 0
        for item in warehouse1:
            if item == item_name:
                amount1 += 1
        amount2 = 0
        for item in warehouse2:
            if item == item_name:
                amount2 += 1

        total_amount = amount1 + amount2
        print(f"Amount available: {total_amount}")

        if item_name in warehouse1 and item_name not in warehouse2:
            print("Location: Warehouse 2")

        elif item_name in warehouse1 and item_name in warehouse2:
            print("Location: both warehouses")
            if amount1 > amount2:
                print(f"In Warehouse 1 the amount is higher. amount: {amount1}")
            elif amount1 == amount2:
                print(f"The amount of items is the same in both warehouses: {amount1}")
            else:
                print(f"In Warehouse 2 the amount is higher. amount: {amount2}")


        elif item_name in warehouse2 and item_name not in warehouse1:
            print("Location: Warehouse 2")
        else:
            answer = input(f"Not in stock\nWould you like to search for another item?").lower()
            if answer == "y" or answer == "yes":
                continue
            else:
                x += 1

        if total_amount > 0:
            answer = input(f"Would you like to place an order for {item_name}? ").lower()
            if answer == "y" or answer == "yes":
                how_many = int(input(f"How many {item_name}s would you like? "))
                if 0 < how_many <= total_amount:
                    print(f"Your order: {how_many} {item_name} is placed!")
                    answer = input("Would you like to continue shopping?").lower()
                    if answer == "y" or answer == "yes":
                        continue
                    else:
                        x += 1
                else:
                    answer = input(f"Error!\nThe maximus available is: {total_amount} items, would you like to take it instead? ").lower()
                    if answer == "y" or answer == "yes":
                        print(f"Your order: {total_amount} {item_name} is placed!")
                        answer = input("Would you like to continue shopping?").lower()
                        if answer == "y" or answer == "yes":
                            continue
                        else:
                            x += 1
                    else:
                        x += 1
            else:
                x += 1




elif number == 3:
    print(f"Thank you for your visit, {name}!")
    quit()

else:
    print(f"Error!\n{number} is an invalid operator, please try again.")

print(f"Thank you for your visit, {name}!")