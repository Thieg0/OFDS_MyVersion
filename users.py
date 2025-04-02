# users.py
from abc import ABC, abstractmethod
import datetime


class User(ABC):
    def __init__(self, id, name, email, phone, password):
        self._id = id
        self._name = name
        self._email = email
        self._phone = phone
        self._password = password
        self._address = None
        self._registration_date = datetime.datetime.now()

    @property
    def id(self):
        return self._id

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, value):
        self._name = value

    @property
    def email(self):
        return self._email

    @email.setter
    def email(self, value):
        self._email = value

    @property
    def phone(self):
        return self._phone

    @phone.setter
    def phone(self, value):
        self._phone = value

    @property
    def address(self):
        return self._address

    @address.setter
    def address(self, value):
        self._address = value

    @abstractmethod
    def display_profile(self):
        pass


class Customer(User):
    def __init__(self, id, name, email, phone, password):
        super().__init__(id, name, email, phone, password)
        self._order_history = []
        self._favorite_restaurants = []
        self._payment_methods = []

    def add_order_to_history(self, order):
        self._order_history.append(order)

    def add_favorite_restaurant(self, restaurant):
        if restaurant not in self._favorite_restaurants:
            self._favorite_restaurants.append(restaurant)

    def remove_favorite_restaurant(self, restaurant):
        if restaurant in self._favorite_restaurants:
            self._favorite_restaurants.remove(restaurant)

    def add_payment_method(self, payment_method):
        self._payment_methods.append(payment_method)

    def get_order_history(self):
        return self._order_history

    def get_favorite_restaurants(self):
        return self._favorite_restaurants
    
    def get_password(self):
        return self._password

    def display_profile(self):
        return f"Cliente: {self._name}\nEmail: {self._email}\nTelefone: {self._phone}"


class Owner(User):
    def __init__(self, id, name, email, phone, password):
        super().__init__(id, name, email, phone, password)
        self._restaurants = []

    def add_restaurant(self, restaurant):
        self._restaurants.append(restaurant)

    def remove_restaurant(self, restaurant):
        if restaurant in self._restaurants:
            self._restaurants.remove(restaurant)

    def get_restaurants(self):
        return self._restaurants
    
    def get_password(self):
        return self._password

    def display_profile(self):
        return f"Proprietário: {self._name}\nEmail: {self._email}\nTelefone: {self._phone}\nRestaurantes: {len(self._restaurants)}"
