from abc import ABC, abstractmethod

class Dish(ABC):
    """Interface base para todos os pratos."""
    
    @abstractmethod
    def get_description(self):
        """Retorna a descrição do prato."""
        pass
    
    @abstractmethod
    def get_price(self):
        """Retorna o preço do prato."""
        pass


class BasicDish(Dish):
    """Implementação básica de um prato do menu."""
    
    def __init__(self, name, price, description=""):
        self.name = name
        self.price = price
        self.description = description if description else name
    
    def get_description(self):
        return self.description
    
    def get_price(self):
        return self.price


class DishDecorator(Dish):
    """Classe base para todos os decoradores de pratos."""
    
    def __init__(self, dish):
        self.dish = dish
    
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_price(self):
        pass


class ExtraCheese(DishDecorator):
    """Decorador para adicionar queijo extra."""
    
    def get_description(self):
        return f"{self.dish.get_description()} + queijo extra"
    
    def get_price(self):
        return self.dish.get_price() + 3.00  # Adiciona R$3,00 pelo queijo extra


class ExtraBacon(DishDecorator):
    """Decorador para adicionar bacon."""
    
    def get_description(self):
        return f"{self.dish.get_description()} + bacon"
    
    def get_price(self):
        return self.dish.get_price() + 4.50  # Adiciona R$4,50 pelo bacon


class SpecialSauce(DishDecorator):
    """Decorador para adicionar molho especial."""
    
    def get_description(self):
        return f"{self.dish.get_description()} + molho especial"
    
    def get_price(self):
        return self.dish.get_price() + 2.00  # Adiciona R$2,00 pelo molho especial


class WithoutIngredient(DishDecorator):
    """Decorador para remover um ingrediente."""
    
    def __init__(self, dish, ingredient):
        super().__init__(dish)
        self.ingredient = ingredient
    
    def get_description(self):
        return f"{self.dish.get_description()} - sem {self.ingredient}"
    
    def get_price(self):
        return self.dish.get_price()  # Preço não muda ao remover ingredientes