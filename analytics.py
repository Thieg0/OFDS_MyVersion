import datetime 
from collections import Counter
import matplotlib.pyplot as plt
import io 
import os 

class RestaurantAnalytics:
    def __init__(self, restaurant):
        self.restaurant = restaurant
        self.orders_data = []

    def add_order(self, order, delivery=None):
        order_data = {
            'order_id': id(order),
            'customer_id': order.customer.id,
            'items': order.items.copy(),
            'total_value': order_calculate_total(),
            'datetime': datetime.datetime.now(),
            'status': order.status,
        }

        if delivery:
            order_data['delivery_status'] = delivery.status
            if delivery.estimated_delivery_time:
                order_data['estimated_delivery_time'] = delivery.estimated_delivery_time
            if hasattr(delivery, 'delivery_time'):
                order_data['actual_delivery_time'] = delivery.delivery_time

        self.orders_data.append(order_data)

    def get_total_orders(self):
        return len(self.orders_data)
    
    def get_total_revenue(self):
        return sum(order['total_value'] for order in self.orders_data)
    
