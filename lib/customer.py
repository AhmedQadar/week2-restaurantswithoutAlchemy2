from lib.review import *
class Customer:
    #list to store instances of Customer class
    _all = []
    
    def __init__(self, name):
        # Add current instance to the _all list
        Customer._all.append(self)
        # Set the name attribute of the instance
        self._name = name


    @property
    def name(self): # Getter method for the name attribute
        return self._name
    

    @name.setter
    def name(self, name):   # Setter method for the name attribute
        self._name = name

    def add_review(restaurant, content): # Create a new Review instance
        Review(restaurant, self, content)

    @classmethod
    def all(cls):
        return cls._all   # Return the list of all instances of the Customer class

    @classmethod
    def find_all_by_name(cls, name):
        return [customer for customer in cls.all() if customer.name == name]  # Find all instances with matching names

    @classmethod
    def find_by_name(cls, name):
        return [customer for customer in cls.all() if customer.name == name][0]  # Find the first instance with a matching name