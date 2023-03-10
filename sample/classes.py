from datetime import datetime


class Warehouse:
    def __init__(self, warehouse_id: int):
        '''
        constractor, takes the num of the warehouse and list the items in it
        '''
        self.warehouse_id = warehouse_id
        self.stock = []

    def occupancy(self):
        '''
        returns int of the len of list of items
        '''
        return len(self.stock)

    def add_item(self, item):
        '''
        to add item to the list of items
        '''
        self.stock.append(item)

    def search_item(self, search_term):
        '''
        to find a specific item in the list of items
        '''
        matching_items = []
        for i in self.stock:
            if search_term.lower() == i:
                matching_items.append(i)
        return matching_items


class Item:
    def __init__(self, state: str, category: str, date_of_stock: datetime, warehouse: int):
        self.state = state
        self.category = category
        self.date_of_stock = date_of_stock

    def __str__(self):
        return f"Item: {self.state} {self.category}"


class User:
    def __init__(self, user_name: str = "Anonymous"):
        '''
        constractor, protected property name
        '''
        self._name = user_name
        self.is_authenticated = False

    def authenticate(self, password: str) -> bool:
        '''
        for now this does nothing
        '''
        return False

    def is_named(self, name: str) -> bool:
        '''
        checks if the given name is equals to the name in the system
        '''
        if name == self._name:
            return True

        return False

    def greet(self):
        print(f"""Hello, {self._name}!
        Welcome to our Warehouse Database.
        If you don't find what you are looking for,
        please ask one of our staff members to assist you.""")

    def bye(self):
        return f"Thank you for your visit, {self._name}!"


class Employee(User):       # this class is for users that are also employees
    def __init__(self, user_name, password, head_of=None):
        '''
        constractor, takes the uer name from super
        private property password
        '''
        User.__init__(self, user_name)
        self.__password = password
        if head_of == "":
            self.head_of = []
        else:
            self.head_of = head_of

    def authenticate(self, password):
        '''
        checks if the given password is matching to the system password
        '''
        return password == self.__password

    def order(self):
        '''
        print the item and the amount that been ordered
        '''
        print(f"Your order for: {self.state} {self.category} amount: {self.occupancy()}, has been placed")

    def greet(self):
        print(f"""Hello, {self._name}!
              If you experience a problem with the system,
              please contact technical support.""")

    def bye(self):
        '''
        returns list of all the actions the employee did with the system
        '''
        User.bye(self)             # todo: create list of user actions
        print("Your actions summary:")
        list_of_actions = []
        for action in list_of_actions:
            print(action)


