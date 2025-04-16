from payment import Payment

class OrderBuilder:
    def __init__(self, customer, restaurant):
        from order import Order

        self._order = Order(customer, restaurant)
        self._items = {}
        self._delivery_instructions = ""
        self._delivery_time_preference = None
        self._payment_method = None
        self._promo_code = None

    def add_item(self, item, quantity = 1):
        if not self._order.restaurant.menu.has_dish(item):
            raise ValueError(f"Item '{item}' não encontrado no menu do restaurante.")

        if item in self._items:
            self._items[item] += quantity
        else:
            self._items[item] = quantity

        return self
    
    def remove_item(self, item):
        if item in self._items:
            del self._items[item]
        else:
            raise ValueError(f"Item '{item}' não encontrado no pedido.")

        return self
    
    def with_delivery_instructions(self, instructions):
        self._delivery_instructions = instructions
        return self
    
    def with_delivery_time(self, time_preference):
        self._delivery_time_preference = time_preference
        return self
    
    def with_payment_method(self, payment_method):
        if not isinstance(payment_method, Payment):
            raise ValueError("Invalid payment method.")
        
        self._payment_method = payment_method
        return self

    def with_promo_code(self, promo_code):
        self._promo_code = promo_code
        return self
    
    def build(self):
        for item, quantity in self._items.items():
            self._order.add_item(item, quantity)

        if self._delivery_instructions:
            self._order.set_delivery_instructions(self._delivery_instructions)

        if self._delivery_time_preference:
            self._order.set_delivery_time_preference(self._delivery_time_preference)

        if self._payment_method:
            self._order.set_payment_method(self._payment_method)

        if self._promo_code:
            self._order.apply_promo_code(self._promo_code)

        return self._order
    
    def reset(self):
        from order import Order

        self._order = Order(self._order.customer, self._order.restaurant)
        self._items = {}
        self._delivery_instructions = ""
        self._delivery_time_preference = None
        self._payment_method = None
        self._promo_code = None

        return self
    
