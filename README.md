#RESTAURANT

class Restaurant:: This line defines a new class named Restaurant.

_all = []: This line creates a class variable _all that is initialized as an empty list. This variable will be used to store instances of the Restaurant class.

def init(self, name):: This line defines the constructor method for the Restaurant class. It takes a parameter name and initializes an instance variable _name with the value of name.

self._name = name: This line assigns the value of the name parameter to the instance variable _name.

Restaurant._all.append(self): This line appends the current instance of the Restaurant class to the _all list. This allows us to keep track of all the instances of Restaurant created.

@property: This is a decorator that defines a getter method for the name property.

-def name(self):: This line defines the getter method for the name property.
return self._name: This line returns the value of the instance variable _name.

@name.setter: This is a decorator that defines a setter method for the name property.

def name(self, name):: This line defines the setter method for the name property.

self._name = name: This line assigns the value of the name parameter to the instance variable _name.

@property: This is a decorator that defines a getter method for the reviews property.

def reviews(self):: This line defines the getter method for the reviews property.

return [review for review in Review.all() if review.restaurant == self]: This line returns a list comprehension that filters the Review.all() list to only include reviews where the restaurant attribute matches the current instance of Restaurant.

@property: This is a decorator that defines a getter method for the customers property.

def customers(self):: This line defines the getter method for the customers property.

return [review.customer for review in self.reviews]: This line returns a list comprehension that extracts the customer attribute from each review in the self.reviews list.

@classmethod: This is a decorator that defines a class method.

def all(cls):: This line defines the class method all that takes the cls parameter (representing the class itself).

return cls._all: This line returns the _all list, which contains all instances of the Restaurant class.

@classmethod: This is a decorator that defines a class method.

def find_all_by_name(cls, name):: This line defines the class method find_all_by_name that takes the cls parameter (representing the class itself) and the name parameter.

return [restaurant for restaurant in cls.all() if restaurant.name == name]: This line returns a list comprehension that filters the cls.all() list to only include restaurants where the name attribute matches the given name.

@classmethod: This is a decorator that defines a class method.

def find_by_name(cls, name):: This line defines the class method find_by_name that takes the cls parameter (representing the class itself) and the name parameter.

 - return [restaurant for restaurant in cls.all() if restaurant.name == name][0]: This line returns the first restaurant found in the cls.all() list where the name attribute matches the given name.
REVIEW
class Review:: This line defines a new class named Review.

_all = []: This line creates a class variable _all that is initialized as an empty list. This variable will be used to store instances of the Review class.

def init(self, restaurant, customer, content):: This line defines the constructor method for the Review class. It takes three parameters: restaurant, customer, and content.

self._content = content: This line assigns the value of the content parameter to the instance variable _content.

Review._all.append(self): This line appends the current instance of the Review class to the _all list. This allows us to keep track of all the instances of Review created.

@classmethod: This is a decorator that defines a class method.

def all(cls):: This line defines the class method all that takes the cls parameter (representing the class itself).

return cls._all: This line returns the _all list, which contains all instances of the Review class.

@property: This is a decorator that defines a getter method for the customer property.

def customer(self):: This line defines the getter method for the customer property.

return self._customer: This line returns the value of the instance variable _customer.

@property: This is a decorator that defines a getter method for the content property.

def content(self):: This line defines the getter method for the content property.

return self._content: This line returns the value of the instance variable _content.

@property: This is a decorator that defines a getter method for the restaurant property.

def restaurant(self):: This line defines the getter method for the restaurant property.

return self._restaurant: This line returns the value of the instance variable _restaurant.

#CUSTOMER

from lib.review import *: This line imports the Review class from the lib.review module.
class Customer:: This line defines a new class named Customer.
_all = []: This line creates a class variable _all that is initialized as an empty list. This variable will be used to store instances of the Customer class.
def __init__(self, name):: This line defines the constructor method for the Customer class. It takes a parameter name.
Customer._all.append(self): This line appends the current instance of the Customer class to the _all list. This allows us to keep track of all the instances of Customer created.
self._name = name: This line assigns the value of the name parameter to the instance variable _name.
@property: This is a decorator that defines a getter method for the name property.
def name(self):: This line defines the getter method for the name property.
return self._name: This line returns the value of the instance variable _name.
@name.setter: This is a decorator that defines a setter method for the name property.
def name(self, name):: This line defines the setter method for the name property.
self._name = name: This line assigns the value of the name parameter to the instance variable _name.
def add_review(restaurant, content):: This line defines a method named add_review that takes two parameters: restaurant and content. This method is used to add a new review for the 
 customer.
Review(restaurant, self, content): This line creates a new instance of the Review class, passing the restaurant, self (the current instance of Customer), and content as arguments.
@classmethod: This is a decorator that defines a class method.
def all(cls):: This line defines the class method all that takes the cls parameter (representing the class itself).
return cls._all: This line returns the _all list, which contains all instances of the Customer class.
@classmethod: This is a decorator that defines a class method.
def find_all_by_name(cls, name):: This line defines the class method find_all_by_name that takes the cls parameter (representing the class itself) and the name parameter.
return [customer for customer in cls.all() if customer.name == name]: This line returns a list comprehension that filters the cls.all() list to only include customers where the name 
attribute matches the given name.
@classmethod: This is a decorator that defines a class method.
def find_by_name(cls, name):: This line defines the class method find_by_name that takes the cls parameter (representing the class itself) and the name parameter.
return [customer for customer in cls.all() if customer.name == name][0]: This line returns the first customer found in the cls.all() list where the name attribute matches the given 
name.