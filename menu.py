from permissions import PermissionManager
from dish_decorator import BasicDish, ExtraCheese, ExtraBacon, SpecialSauce, WithoutIngredient


class Menu:
    def __init__(self, restaurant):
        self._dishes = {}  # Agora armazena objetos BasicDish em vez de apenas preços
        self._restaurant = restaurant

    def _check_owner_permission(self, user):
        PermissionManager.check_restaurant_owner_permission(user, self._restaurant)

    def add_dish(self, user, dish_name, price, description=""):
        self._check_owner_permission(user)
        self._dishes[dish_name] = BasicDish(dish_name, price, description)

    def update_dish_price(self, user, dish_name, new_price):
        self._check_owner_permission(user)
        if dish_name in self._dishes:
            dish = self._dishes[dish_name]
            description = dish.get_description()
            self._dishes[dish_name] = BasicDish(dish_name, new_price, description)
        else:
            raise ValueError(f"Prato '{dish_name}' não encontrado no menu.")

    def remove_dish(self, user, dish_name):
        self._check_owner_permission(user)
        if dish_name in self._dishes:
            del self._dishes[dish_name]
        else:
            raise ValueError(f"Prato '{dish_name}' não encontrado no menu.")

    def display_menu(self):
        menu_text = []
        for name, dish in self._dishes.items():
            menu_text.append(f"{name}: {dish.get_description()} - R${dish.get_price():.2f}")
        return "\n".join(menu_text)
    
    def get_dish_price(self, dish_name):
        """Retorna o preço de um prato específico."""
        if dish_name in self._dishes:
            return self._dishes[dish_name].get_price()
        else:
            raise ValueError(f"Prato '{dish_name}' não encontrado no menu.")
            
    def has_dish(self, dish_name):
        """Verifica se um prato existe no menu."""
        return dish_name in self._dishes
        
    def get_dish(self, dish_name):
        """Retorna o objeto Dish."""
        if dish_name in self._dishes:
            return self._dishes[dish_name]
        else:
            raise ValueError(f"Prato '{dish_name}' não encontrado no menu.")
    
    def get_all_dishes(self):
        """Retorna uma cópia do dicionário de pratos."""
        return self._dishes.copy()