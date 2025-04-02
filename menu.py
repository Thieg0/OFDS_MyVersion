# menu.py
from permissions import PermissionManager

class Menu:
    def __init__(self, restaurant):
        self._dishes = {}
        self._restaurant = restaurant

    def _check_owner_permission(self, user):
        PermissionManager.check_restaurant_owner_permission(user, self._restaurant)

    def add_dish(self, user, dish_name, price):
        self._check_owner_permission(user)
        self._dishes[dish_name] = price

    def update_dish_price(self, user, dish_name, new_price):
        self._check_owner_permission(user)
        if dish_name in self._dishes:
            self._dishes[dish_name] = new_price
        else:
            raise ValueError(f"Prato '{dish_name}' não encontrado no menu.")

    def remove_dish(self, user, dish_name):
        self._check_owner_permission(user)
        if dish_name in self._dishes:
            del self._dishes[dish_name]
        else:
            raise ValueError(f"Prato '{dish_name}' não encontrado no menu.")

    def display_menu(self):
        return "\n".join([f"{dish}: R${price:.2f}" for dish, price in self._dishes.items()])
    
    def get_dish_price(self, dish_name):
        """Retorna o preço de um prato específico."""
        if dish_name in self._dishes:
            return self._dishes[dish_name]
        else:
            raise ValueError(f"Prato '{dish_name}' não encontrado no menu.")
            
    def has_dish(self, dish_name):
        """Verifica se um prato existe no menu."""
        return dish_name in self._dishes
        
    def get_all_dishes(self):
        """Retorna uma cópia do dicionário de pratos."""
        return self._dishes.copy()