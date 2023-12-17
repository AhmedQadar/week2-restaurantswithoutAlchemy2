class Restaurant:
    # List to store instances of the Restaurant class
    _all = [] 
    def __init__(self, name):
        self._name = name    # Set the name attribute of the instance
        Restaurant._all.append(self) # Add current instance to the _all list

    @property
    def name(self):  # Getter method for the name attribute
        return self._name

    @name.setter
    def name(self, name):  # Setter method for the name attribute
        self._name = name

    @property
    def reviews(self): # Getter method that returns a list of reviews for this restaurant
        return [review for review in Review.all() if review.restaurant == self]

    @property
    def customers(self): # Getter method that returns a list of customers who reviewed this restaurant
        return [review.customer for review in self.reviews]

    @classmethod
    def all(cls): # Return the list of all instances of the Restaurant class
        return cls._all

    @classmethod
    def find_all_by_name(cls, name): # Find all instances of the Restaurant class with matching names
        return [restaurant for restaurant in cls.all() if restaurant.name == name]

    @classmethod
    def find_by_name(cls, name):
        return [restaurant for restaurant in cls.all() if restaurant.name == name][0]



