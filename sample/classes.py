from datetime import datetime


class Warehouse:
    def __init__(self, warehouse_id: int):
        """
        constractor,  num of the warehouse and list of the items in it
        """
        self.warehouse_id = warehouse_id
        self.stock = []

    def occupancy(self):
        """
        returns int of the len of list of items
        """
        return len(self.stock)

    def add_item(self, item):
        """
        to add item to the list of items
        """
        self.stock.append(item)

    def search_item(self, search_term):
        """
        to find items that are matching to the search term, lopping a list of Item object
        """
        matching_items = []
        for i in self.stock:
            if search_term.lower() == (i.state + " " + i.category).lower():
                matching_items.append(i)
        return matching_items


class Item:
    def __init__(self, state: str, category: str, warehouse: int, date_of_stock: datetime):
        self.state = state
        self.category = category
        self.warehouse = warehouse
        self.date_of_stock = date_of_stock

    def __str__(self):
        return f"Item: {self.state} {self.category}"


class User:
    def __init__(self, user_name: str = "Anonymous"):
        """
        constractor, protected property name
        """
        self._name = user_name
        self.is_authenticated = False

    def authenticate(self, password: str) -> bool:
        """
        for now this does nothing
        """
        return False

    def is_named(self, name: str) -> bool:
        """
        checks if the given name is equals to the name in the system
        """
        if name == self._name:
            return True

        return False

    def greet(self):
        print(f"""Hello, {self._name}!
        Welcome to our Warehouse Database.
        If you don't find what you are looking for,
        please ask one of our staff members to assist you.""")

    def bye(self):
        print(f"Thank you for your visit, {self._name}!")

    @property
    def name(self):
        """name getter"""
        return self._name


class Employee(User):
    list_of_actions = []  # list to sum employee actions

    def __init__(self, user_name, password, head_of=None):
        """
        constractor, takes the uer name from super
        private property password
        """
        super().__init__(user_name)  # -> attribute from user= _name
        self.__password = password
        if head_of is not None:
            self.head_of = []
            for i in head_of:
                if "head_of" in i.keys():
                    self.head_of.append(Employee(i["user_name"], i["password"], i["head_of"]))
                else:
                    self.head_of.append(Employee(i["user_name"], i["password"]))

        else:
            self.head_of = head_of

    def get_password(self):
        """getter for the private attribute password"""
        return self.__password

    def authenticate(self, password):
        """
        checks if the given password is matching to the system password
        """
        return password == self.__password

    def order(self, item_name, amount):
        """
        print the item and the amount that been ordered
        """
        print(f"Your order for: {item_name} amount: {amount}, has been placed!")

    def greet(self):
        print(f"""Hello, {self._name}!
              If you experience a problem with the system,
              please contact technical support.""")

    def bye(self):
        """
        returns bye message list of all the actions the employee did with the system
        """
        User.bye(self)
        print("Your actions summary:")
        for index, action in enumerate(Employee.list_of_actions):
            print(index + 1, ".", action)
