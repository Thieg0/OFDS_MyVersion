from abc import ABC, abstractmethod

class DeliveryObserver(ABC):
    """
    Abstract base class for observers that want to be notified of delivery status changes.
    """

    @abstractmethod
    def update(self, delivery):
        """
        Update the observer with the new delivery status.
        """
        pass

class CustomerNotifier(DeliveryObserver):
    """
    Concrete observer that notifies the customer of delivery status changes.
    """
    def __init__(self, customer):
        self.customer = customer

    def update(self, delivery):
        """
        Notify the customer of the delivery status change.
        """
        message = f"Olá {self.customer}, seu pedido está agora em status: {delivery.status}."

        # In a real-world scenario, this would send an SMS or email.
        print(f"[Notificação SMS] {message}")

        # Store the notification in the customer's record
        if not hasattr(self.customer, 'notifications'):
            self.customer.notifications = []
        self.customer.notifications.append({
            'timestamp': delivery.status_history[-1]['timestamp'],
            'message': message
        })

class RestaurantNotifier(DeliveryObserver):
    """
    Concrete observer that notifies the restaurant of delivery status changes.
    """
    def __init__(self, restaurant):
        self.restaurant = restaurant

    def update(self, delivery):
        """
        Notify the restaurant of the delivery status change.
        """
        message = f"Status do pedido #{id(delivery.order)} atualizado para: {delivery.status}."

        # In a real-world scenario, this would send an notification for the restaurant's dashboard.
        print(f"[Notificação Restaurante] {message}")

class AnalyticsTracker(DeliveryObserver):
    """
    Concrete observer that register data of delivery to analytics.
    """

    def update(self, delivery):
        """
        Register the change of status in the analytics system.
        """
        delivery.order.restaurant.analytics.add_order_data(delivery.order, delivery)
        print(f"[Analytics] Dados do pedido #{id(delivery.order)} registrados com status: {delivery.status}.")

class DeliverySubject:
    # Class for objects that can be observed by delivery observers.
    def __init__(self):
        self._observers = []

    def attach(self, observer):
        """
        Attach an observer to the subject.
        """
        if observer not in self._observers:
            self._observers.append(observer)

    def detach(self, observer):
        """
        Detach an observer from the subject.
        """
        try:
            self._observers.remove(observer)
        except ValueError:
            pass

    def notify(self):
        """
        Notify all observers of a change in the subject's state.
        """
        print(f"[DEBUG] Notificando {len(self._observers)} observadores")
        for observer in self._observers:
            print(f"[DEBUG] Notificando observador: {type(observer).__name__}")
            observer.update(self)