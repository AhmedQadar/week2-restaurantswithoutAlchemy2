class Review:
     # List to store instances of the Review class
    _all = [] 

    def __init__(self, restaurant, customer, content):
        self._content = content # Set the content attribute of the instance
        Review._all.append(self) # Add current instance to the _all list


    @classmethod
    def all(cls): # Return the list of all instances of the Review class
        return cls._all


    @property
    def customer(self):# Getter method for the customer attribute
        return self._customer

    @property
    def content(self):# Getter method for the content attribute
        return self._content

    @property
    def restaurant(self):  # Getter method for the restaurant attribute
        return self._restaurant



