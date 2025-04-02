class PermissionManager:
    @staticmethod
    def is_customer(user):
        """Verifica se um usuário é um cliente."""
        return hasattr(user, "add_favorite_restaurant")
    
    @staticmethod
    def is_owner(user):
        """Verifica se um usuário é um proprietário."""
        return hasattr(user, "get_restaurants")
    
    @staticmethod
    def is_restaurant_owner(user, restaurant):
        """Verifica se um usuário é o proprietário de um restaurante específico."""
        return user.id == restaurant.owner.id
    
    @staticmethod
    def check_customer_permission(user):
        """Verifica se o usuário é um cliente e levanta uma exceção caso contrário."""
        if not PermissionManager.is_customer(user):
            raise PermissionError("Esta ação só pode ser realizada por clientes.")
    
    @staticmethod
    def check_owner_permission(user):
        """Verifica se o usuário é um proprietário e levanta uma exceção caso contrário."""
        if not PermissionManager.is_owner(user):
            raise PermissionError("Esta ação só pode ser realizada por proprietários de restaurantes.")
    
    @staticmethod
    def check_restaurant_owner_permission(user, restaurant):
        """Verifica se o usuário é o proprietário de um restaurante específico."""
        if not PermissionManager.is_restaurant_owner(user, restaurant):
            raise PermissionError("Esta ação só pode ser realizada pelo proprietário deste restaurante.")