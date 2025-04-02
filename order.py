# order.py
class Order:
    def __init__(self, customer, restaurant):
        self.customer = customer
        self.restaurant = restaurant
        self.items = {}
        self.status = "Em preparo"
        self.payment_method = None
        self.delivery_instructions = ""
        self.delivery_time_preference = None  # Horário preferido para entrega

    def add_item(self, item, quantity):
        if self.restaurant.menu.has_dish(item):
            if item in self.items:
                self.items[item] += quantity
            else:
                self.items[item] = quantity
        else:
            raise ValueError(f"Item '{item}' não encontrado no menu.")

    def remove_item(self, item):
        if item in self.items:
            del self.items[item]
        else:
            raise ValueError(f"Item '{item}' não encontrado no pedido.")

    def calculate_total(self):
        total = 0
        for item, quantity in self.items.items():
            total += self.restaurant.menu.get_dish_price(item) * quantity
        return total

    def set_payment_method(self, payment_method):
        """Define o método de pagamento para o pedido."""
        self.payment_method = payment_method
        
    def set_delivery_instructions(self, instructions):
        """Define instruções especiais para a entrega."""
        self.delivery_instructions = instructions
        
    def set_delivery_time_preference(self, time_preference):
        """Define o horário preferido para entrega."""
        self.delivery_time_preference = time_preference

    def display_order(self):
        order_details = "\n".join([f"{item}: {quantity}x" for item, quantity in self.items.items()])
        total = self.calculate_total()
        
        result = f"Pedido de {self.customer.name}:\n{order_details}\nTotal: R${total:.2f}"
        
        if self.delivery_instructions:
            result += f"\nInstruções de entrega: {self.delivery_instructions}"
            
        if self.delivery_time_preference:
            result += f"\nHorário preferido: {self.delivery_time_preference}"
            
        if self.payment_method:
            result += f"\nMétodo de pagamento: {type(self.payment_method).__name__}"
            
        return result