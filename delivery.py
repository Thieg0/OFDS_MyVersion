# delivery.py
import datetime
import random  # Para simular coordenadas de localização na demonstração
from observer import DeliverySubject


class DeliveryLocation:
    """Classe para armazenar e gerenciar a localização do entregador."""
    
    def __init__(self, latitude=0.0, longitude=0.0):
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = datetime.datetime.now()
    
    def update_location(self, latitude, longitude):
        """Atualiza a localização atual."""
        self.latitude = latitude
        self.longitude = longitude
        self.timestamp = datetime.datetime.now()
        
    def get_location_info(self):
        """Retorna informações de localização formatadas."""
        return {
            "latitude": self.latitude,
            "longitude": self.longitude,
            "timestamp": self.timestamp,
            "formatted": f"Lat: {self.latitude:.6f}, Long: {self.longitude:.6f}"
        }


class Delivery(DeliverySubject):
    """Classe para gerenciar a entrega de um pedido."""
    
    # Status possíveis para uma entrega
    STATUS_PREPARING = "Em preparo"
    STATUS_READY = "Pronto para entrega"
    STATUS_ASSIGNED = "Entregador designado"
    STATUS_PICKED_UP = "Pedido coletado"
    STATUS_ON_THE_WAY = "A caminho"
    STATUS_NEAR = "Próximo ao destino"
    STATUS_ARRIVED = "Chegou ao destino"
    STATUS_DELIVERED = "Entregue"
    STATUS_CANCELLED = "Cancelado"
    
    def __init__(self, order):
        DeliverySubject.__init__(self)
        self.order = order
        self.status = self.STATUS_PREPARING
        self.status_history = []
        self.add_status_update(self.status)
        
        self.delivery_person = None  # Nome do entregador
        self.estimated_delivery_time = None  # Tempo estimado de entrega
        self.location = DeliveryLocation()  # Localização atual
        self.delivery_notes = ""  # Notas adicionais sobre a entrega
        
    def add_status_update(self, status, notes=""):
        """Adiciona uma atualização de status ao histórico."""
        update = {
            "status": status,
            "timestamp": datetime.datetime.now(),
            "notes": notes
        }
        self.status_history.append(update)
        self.status = status
        
    def update_status(self, new_status, notes=""):
        """Atualiza o status da entrega."""
        valid_statuses = [
            self.STATUS_PREPARING,
            self.STATUS_READY,
            self.STATUS_ASSIGNED,
            self.STATUS_PICKED_UP,
            self.STATUS_ON_THE_WAY,
            self.STATUS_NEAR,
            self.STATUS_ARRIVED,
            self.STATUS_DELIVERED,
            self.STATUS_CANCELLED
        ]
        
        if new_status in valid_statuses:
            self.add_status_update(new_status, notes)
            
            # Configurar tempo estimado de entrega quando o status mudar para "A caminho"
            if new_status == self.STATUS_ON_THE_WAY and not self.estimated_delivery_time:
                # Estima entre 20 e 40 minutos a partir de agora
                minutes = random.randint(20, 40)
                self.estimated_delivery_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)

            print(f"[DEBUG] Atualizando status para {new_status}. Preparando para notificar observadores.")

            self.notify()
            
            return True
        else:
            raise ValueError(f"Status '{new_status}' inválido.")
    
    def assign_delivery_person(self, name):
        """Designa um entregador para o pedido."""
        self.delivery_person = name
        self.update_status(self.STATUS_ASSIGNED, f"Entregador {name} designado")
        
    def update_location(self, latitude, longitude):
        """Atualiza a localização atual do entregador."""
        self.location.update_location(latitude, longitude)
        
        # Quando a localização é atualizada, podemos atualizar o status com base na proximidade
        # Para fins de demonstração, vamos usar valores aleatórios
        if self.status == self.STATUS_ON_THE_WAY and random.random() > 0.7:
            self.update_status(self.STATUS_NEAR, "Entregador está próximo ao seu endereço")
        
    def update_estimated_time(self, minutes):
        """Atualiza o tempo estimado de entrega."""
        self.estimated_delivery_time = datetime.datetime.now() + datetime.timedelta(minutes=minutes)
    
    def add_delivery_note(self, note):
        """Adiciona uma nota sobre a entrega."""
        self.delivery_notes += f"[{datetime.datetime.now().strftime('%H:%M:%S')}] {note}\n"
    
    def get_tracking_link(self):
        """Retorna um link fictício para rastreamento (em uma aplicação real, isso seria um link real)."""
        # Em uma implementação real, isso geraria um link único para rastreamento
        order_id = id(self.order)  # Usando o ID do objeto como exemplo
        return f"https://fooddelivery.example.com/track/{order_id}"
    
    def simulate_delivery_progress(self):
        """
        Método para simular o progresso da entrega para fins de demonstração.
        Em uma aplicação real, isso seria atualizado com base em dados reais do entregador.
        """
        current_status = self.status
        
        # Simula a progressão do status
        if current_status == self.STATUS_PREPARING:
            self.update_status(self.STATUS_READY, "Seu pedido está pronto para ser coletado")
        elif current_status == self.STATUS_READY:
            self.assign_delivery_person(f"Entregador #{random.randint(1000, 9999)}")
        elif current_status == self.STATUS_ASSIGNED:
            self.update_status(self.STATUS_PICKED_UP, "Entregador pegou seu pedido no restaurante")
            # Simula coordenadas iniciais (em uma aplicação real, seriam as coordenadas do restaurante)
            self.update_location(-9.6498 + random.uniform(-0.01, 0.01), -35.7089 + random.uniform(-0.01, 0.01))
        elif current_status == self.STATUS_PICKED_UP:
            self.update_status(self.STATUS_ON_THE_WAY, "Entregador está a caminho do seu endereço")
            # Simula movimento do entregador
            self.update_location(
                self.location.latitude + random.uniform(-0.005, 0.005),
                self.location.longitude + random.uniform(-0.005, 0.005)
            )
        elif current_status == self.STATUS_ON_THE_WAY:
            # Atualiza a localização para simular movimento
            self.update_location(
                self.location.latitude + random.uniform(-0.005, 0.005),
                self.location.longitude + random.uniform(-0.005, 0.005)
            )
            # Às vezes atualiza para "próximo"
            if random.random() > 0.7:
                self.update_status(self.STATUS_NEAR, "Entregador está próximo ao seu endereço")
        elif current_status == self.STATUS_NEAR:
            self.update_status(self.STATUS_ARRIVED, "Entregador chegou ao seu endereço")
        elif current_status == self.STATUS_ARRIVED:
            self.update_status(self.STATUS_DELIVERED, "Pedido entregue com sucesso!")
    
    def display_status(self):
        """Exibe o status atual e informações de rastreamento."""
        result = f"Status do pedido: {self.status}\n"
        
        if self.delivery_person:
            result += f"Entregador: {self.delivery_person}\n"
        
        if self.estimated_delivery_time and self.status not in [self.STATUS_DELIVERED, self.STATUS_CANCELLED]:
            now = datetime.datetime.now()
            if now < self.estimated_delivery_time:
                # Calcula o tempo restante
                time_diff = self.estimated_delivery_time - now
                minutes_remaining = int(time_diff.total_seconds() / 60)
                result += f"Tempo estimado de entrega: {minutes_remaining} minutos\n"
            else:
                result += "Seu pedido está atrasado, mas está a caminho!\n"
        
        # Adiciona o link de rastreamento
        if self.status not in [self.STATUS_PREPARING, self.STATUS_READY, self.STATUS_DELIVERED, self.STATUS_CANCELLED]:
            result += f"Link para rastreamento: {self.get_tracking_link()}\n"
        
        # Adiciona a localização atual se estiver a caminho
        if self.status in [self.STATUS_ON_THE_WAY, self.STATUS_NEAR, self.STATUS_ARRIVED]:
            loc_info = self.location.get_location_info()
            result += f"Localização atual: {loc_info['formatted']}\n"
        
        # Adiciona histórico de status
        result += "\nHistórico de status:\n"
        for update in self.status_history:
            status_time = update["timestamp"].strftime("%H:%M:%S")
            status_text = f"• {status_time} - {update['status']}"
            if update["notes"]:
                status_text += f": {update['notes']}"
            result += status_text + "\n"
        
        return result