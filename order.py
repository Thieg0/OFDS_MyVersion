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
            # Verifica se é um prato personalizado
            if hasattr(self, 'custom_dishes') and item in self.custom_dishes:
                total += self.custom_dishes[item].get_price() * quantity
            else:
                # Prato normal do menu
                total += self.restaurant.menu.get_dish_price(item) * quantity
        return total
    
    def end_order(self, delivery=None):
        self.status = "Finalizado"
        self.restaurant.analytics.add_order_data(self, delivery)
        self.customer.add_order_to_history(self)
        return 'Pedido finalizado com sucesso!'
    
    def apply_promo_code(self, promo_code):
        try:
            self.total_with_discount = self.restaurant.promotions.apply_promotion(promo_code, self.calculate_total())
            self.applied_promo_code = promo_code
            return True
        except ValueError:
            return False

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
        order_details = []
        for item, quantity in self.items.items():
            # Verifica se é um prato personalizado
            if hasattr(self, 'custom_dishes') and item in self.custom_dishes:
                dish = self.custom_dishes[item]
                order_details.append(f"{dish.get_description()}: {quantity}x - R${dish.get_price():.2f}/unidade")
            else:
                # Prato normal do menu
                price = self.restaurant.menu.get_dish_price(item)
                order_details.append(f"{item}: {quantity}x - R${price:.2f}/unidade")
        
        order_text = "\n".join(order_details)
        total = self.calculate_total()
        
        result = f"Pedido de {self.customer.name}:\n{order_text}\nTotal: R${total:.2f}"

        if hasattr(self, 'applied_promo_code') and hasattr(self, 'total_with_discount'):
            discount = total - self.total_with_discount
            result += f"\nCódigo promocional aplicado: {self.applied_promo_code}"
            result += f"\nDesconto: R${discount:.2f}"
            result += f"\nTotal com desconto: R${self.total_with_discount:.2f}"
        
        if self.delivery_instructions:
            result += f"\nInstruções de entrega: {self.delivery_instructions}"
            
        if self.delivery_time_preference:
            result += f"\nHorário preferido: {self.delivery_time_preference}"
            
        if self.payment_method:
            result += f"\nMétodo de pagamento: {type(self.payment_method).__name__}"
            
        return result