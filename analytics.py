import datetime 
from collections import Counter
import matplotlib.pyplot as plt
import io 
import os 

class RestaurantAnalytics:
    """Classe para análise de dados de um restaurante."""
    
    def __init__(self, restaurant):
        """Inicializa o analytics para um restaurante específico."""
        self.restaurant = restaurant
        self.orders_data = []  # Lista de pedidos para análise
        
    def add_order_data(self, order, delivery=None):
        """Adiciona dados de um pedido ao analytics."""
        order_data = {
            "order_id": id(order),  # Usando o ID do objeto como identificador único
            "customer_id": order.customer.id,
            "items": order.items.copy(),
            "total_value": order.calculate_total(),
            "datetime": datetime.datetime.now(),
            "status": order.status,
        }
        
        if delivery:
            order_data["delivery_status"] = delivery.status
            if delivery.estimated_delivery_time:
                order_data["estimated_delivery_time"] = delivery.estimated_delivery_time
            if hasattr(delivery, "delivery_time"):
                order_data["actual_delivery_time"] = delivery.delivery_time
                
        self.orders_data.append(order_data)
        print("Dados do pedido registrados no analytics com sucesso!")
        
    def get_total_orders(self):
        """Retorna o número total de pedidos."""
        return len(self.orders_data)
    
    def get_total_revenue(self):
        """Retorna a receita total gerada pelos pedidos."""
        return sum(order["total_value"] for order in self.orders_data)
    
    def get_average_order_value(self):
        """Retorna o valor médio dos pedidos."""
        if not self.orders_data:
            return 0
        return self.get_total_revenue() / self.get_total_orders()
    
    def get_most_popular_items(self, limit=5):
        """Retorna os itens mais populares, limitado a 'limit' itens."""
        all_items = []
        for order in self.orders_data:
            for item, quantity in order["items"].items():
                all_items.extend([item] * quantity)
                
        counter = Counter(all_items)
        return counter.most_common(limit)
    
    def get_peak_hours(self):
        """Retorna as horas com mais pedidos."""
        hours = [order["datetime"].hour for order in self.orders_data]
        return Counter(hours)
    
    def get_orders_by_day(self):
        """Retorna o número de pedidos por dia da semana."""
        days = [order["datetime"].strftime("%A") for order in self.orders_data]
        return Counter(days)
    
    def get_customer_retention(self):
        """Retorna estatísticas sobre retenção de clientes."""
        customers = [order["customer_id"] for order in self.orders_data]
        counter = Counter(customers)
        
        # Número de clientes que fizeram pelo menos um pedido
        unique_customers = len(counter)
        
        # Número de clientes que fizeram mais de um pedido
        returning_customers = sum(1 for count in counter.values() if count > 1)
        
        # Taxa de retenção
        retention_rate = (returning_customers / unique_customers) * 100 if unique_customers > 0 else 0
        
        return {
            "unique_customers": unique_customers,
            "returning_customers": returning_customers,
            "retention_rate": retention_rate
        }
    
    def get_delivery_performance(self):
        """Retorna estatísticas sobre o desempenho de entrega."""
        # Filtrando apenas pedidos entregues
        delivered_orders = [
            order for order in self.orders_data 
            if "actual_delivery_time" in order and "estimated_delivery_time" in order
        ]
        
        if not delivered_orders:
            return {
                "total_deliveries": 0,
                "on_time_deliveries": 0,
                "late_deliveries": 0,
                "on_time_percentage": 0,
                "average_delay_minutes": 0
            }
        
        # Pedidos entregues no prazo vs. atrasados
        on_time = sum(
            1 for order in delivered_orders 
            if order["actual_delivery_time"] <= order["estimated_delivery_time"]
        )
        
        late = len(delivered_orders) - on_time
        
        # Calculando atraso médio em minutos
        total_delay = sum(
            (order["actual_delivery_time"] - order["estimated_delivery_time"]).total_seconds() / 60
            for order in delivered_orders
            if order["actual_delivery_time"] > order["estimated_delivery_time"]
        )
        
        average_delay = total_delay / late if late > 0 else 0
        
        return {
            "total_deliveries": len(delivered_orders),
            "on_time_deliveries": on_time,
            "late_deliveries": late,
            "on_time_percentage": (on_time / len(delivered_orders)) * 100,
            "average_delay_minutes": average_delay
        }
    
    def get_dashboard_summary(self):
        """Retorna um resumo do dashboard para exibição no terminal."""
        if not self.orders_data:
            return "Não há dados suficientes para gerar o resumo."
            
        total_orders = self.get_total_orders()
        total_revenue = self.get_total_revenue()
        avg_order = self.get_average_order_value()
        
        popular_items = self.get_most_popular_items(3)  # Top 3 itens
        popular_items_text = "\n".join([f"  - {item}: {count} unidades" for item, count in popular_items])
        
        retention = self.get_customer_retention()
        
        summary = f"""
RESUMO DE DESEMPENHO - {self.restaurant.name}
{'=' * 50}

MÉTRICAS PRINCIPAIS:
- Total de pedidos: {total_orders}
- Receita total: R$ {total_revenue:.2f}
- Valor médio por pedido: R$ {avg_order:.2f}

TOP 3 ITENS MAIS VENDIDOS:
{popular_items_text if popular_items else "  Nenhum item vendido ainda"}

CLIENTES:
- Taxa de retenção: {retention['retention_rate']:.2f}%
  ({retention['returning_customers']} de {retention['unique_customers']} clientes retornaram)

Para visualizar mais detalhes, use as opções específicas do analytics.
"""
        return summary