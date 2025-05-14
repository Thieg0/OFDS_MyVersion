# Padrões de Design Implementados

Este documento descreve os padrões de design adicionados ao sistema de delivery de comida online, destacando como foram implementados e seus benefícios para a aplicação.

## Sumário
1. [Padrão Builder](#padrão-builder)
2. [Padrão Comportamental: Observer](#padrão-observer)
3. [Padrão Estrutural: Decorator](#padrão-decorator)

---

## Padrão Builder

O padrão Builder é utilizado para criar pedidos de forma mais fluente e flexível.

### Principais características
- Permite a criação de pedidos com uma interface fluente
- Facilita a adição de componentes opcionais
- Suporta validação durante a construção
- Permite reutilização do builder para múltiplos pedidos

### Exemplo de uso
```python
order = OrderBuilder(customer, restaurant) \
    .add_item("Pizza", 2) \
    .add_item("Refrigerante", 3) \
    .with_delivery_instructions("Deixar na portaria") \
    .with_delivery_time("19:30") \
    .with_promo_code("DESCONTO10") \
    .build()
```

---

## Padrão Observer

O padrão Observer foi implementado para notificar múltiplas entidades sobre mudanças no status de entrega.

### Motivação
Antes da implementação do Observer, a atualização do status da entrega não notificava automaticamente os interessados. Era necessário que o cliente, o restaurante e o sistema de analytics verificassem manualmente o status da entrega, o que poderia resultar em informações desatualizadas.

### Implementação
1. **Componentes principais**:
   - `DeliveryObserver` (interface): Define o método `update()` que todos os observadores devem implementar
   - `DeliverySubject` (classe base): Mantém uma lista de observadores e notifica-os quando há mudanças
   - Observadores concretos: `CustomerNotifier`, `RestaurantNotifier`, `AnalyticsTracker`

2. **Funcionamento**:
   - A classe `Delivery` herda de `DeliverySubject`
   - Quando o status de uma entrega é atualizado, todos os observadores registrados são notificados
   - Cada observador implementa sua própria lógica de resposta à mudança

### Código Implementado
```python
# Arquivo observer.py
from abc import ABC, abstractmethod

class DeliveryObserver(ABC):
    @abstractmethod
    def update(self, delivery):
        pass

class CustomerNotifier(DeliveryObserver):
    def __init__(self, customer):
        self.customer = customer
    
    def update(self, delivery):
        message = f"Olá {self.customer.name}, o status do seu pedido mudou para: {delivery.status}"
        print(f"[NOTIFICAÇÃO SMS] {message}")
        
        # Armazena a notificação no histórico do cliente
        if not hasattr(self.customer, 'notifications'):
            self.customer.notifications = []
        self.customer.notifications.append({
            'timestamp': delivery.status_history[-1]["timestamp"],
            'message': message
        })

class RestaurantNotifier(DeliveryObserver):
    def __init__(self, restaurant):
        self.restaurant = restaurant
    
    def update(self, delivery):
        message = f"Status do pedido #{id(delivery.order)} atualizado para: {delivery.status}"
        print(f"[NOTIFICAÇÃO RESTAURANTE] {message}")

class AnalyticsTracker(DeliveryObserver):
    def update(self, delivery):
        delivery.order.restaurant.analytics.add_order_data(delivery.order, delivery)
        print(f"[ANALYTICS] Dados de entrega atualizados para o pedido #{id(delivery.order)}")

class DeliverySubject:
    def __init__(self):
        self._observers = []
    
    def attach(self, observer):
        if observer not in self._observers:
            self._observers.append(observer)
    
    def detach(self, observer):
        try:
            self._observers.remove(observer)
        except ValueError:
            pass
    
    def notify(self):
        for observer in self._observers:
            observer.update(self)
```

### Modificações na classe Delivery
```python
# Modificações em delivery.py
class Delivery(DeliverySubject):  # Agora herda de DeliverySubject
    # ... código existente ...
    
    def update_status(self, new_status, notes=""):
        # ... código existente ...
        
        # Notificar todos os observadores sobre a mudança de status
        self.notify()
        
        return True
```

### Benefícios Obtidos
1. **Desacoplamento**: Os componentes do sistema estão desacoplados - o objeto observado não precisa conhecer detalhes dos observadores
2. **Notificações em tempo real**: Clientes e restaurantes são notificados imediatamente sobre mudanças de status
3. **Facilidade de extensão**: Novos observadores podem ser adicionados sem modificar o código existente
4. **Registro automático de dados**: O sistema de analytics é atualizado automaticamente a cada mudança
5. **Experiência do usuário melhorada**: Os clientes recebem notificações proativas sobre seus pedidos

---

## Padrão Decorator

O padrão Decorator foi implementado para personalizar pratos do menu, permitindo adicionar extras e modificações sem alterar as classes originais.

### Motivação
Antes da implementação do Decorator, não era possível personalizar os pratos do menu. Os clientes não podiam adicionar extras (como queijo, bacon ou molho especial) ou remover ingredientes específicos, limitando a flexibilidade do sistema.

### Implementação
1. **Componentes principais**:
   - `Dish` (interface): Define métodos para obter descrição e preço
   - `BasicDish`: Implementação concreta de um prato básico
   - `DishDecorator` (classe abstrata): Base para todos os decoradores
   - Decoradores concretos: `ExtraCheese`, `ExtraBacon`, `SpecialSauce`, `WithoutIngredient`

2. **Funcionamento**:
   - Os pratos básicos são envolvidos por decoradores
   - Cada decorador modifica a descrição e/ou o preço do prato
   - Os decoradores podem ser aninhados para adicionar múltiplas personalizações

### Código Implementado
```python
# Arquivo dish_decorator.py
from abc import ABC, abstractmethod

class Dish(ABC):
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_price(self):
        pass

class BasicDish(Dish):
    def __init__(self, name, price, description=""):
        self.name = name
        self.price = price
        self.description = description if description else name
    
    def get_description(self):
        return self.description
    
    def get_price(self):
        return self.price

class DishDecorator(Dish):
    def __init__(self, dish):
        self.dish = dish
    
    @abstractmethod
    def get_description(self):
        pass
    
    @abstractmethod
    def get_price(self):
        pass

class ExtraCheese(DishDecorator):
    def get_description(self):
        return f"{self.dish.get_description()} + queijo extra"
    
    def get_price(self):
        return self.dish.get_price() + 3.00

class ExtraBacon(DishDecorator):
    def get_description(self):
        return f"{self.dish.get_description()} + bacon"
    
    def get_price(self):
        return self.dish.get_price() + 4.50

class SpecialSauce(DishDecorator):
    def get_description(self):
        return f"{self.dish.get_description()} + molho especial"
    
    def get_price(self):
        return self.dish.get_price() + 2.00

class WithoutIngredient(DishDecorator):
    def __init__(self, dish, ingredient):
        super().__init__(dish)
        self.ingredient = ingredient
    
    def get_description(self):
        return f"{self.dish.get_description()} - sem {self.ingredient}"
    
    def get_price(self):
        return self.dish.get_price()
```

### Modificações na classe Menu
```python
# Modificações em menu.py
from dish_decorator import BasicDish

class Menu:
    # ... código existente ...
    
    def add_dish(self, user, dish_name, price, description=""):
        self._check_owner_permission(user)
        self._dishes[dish_name] = BasicDish(dish_name, price, description)
    
    # ... código existente modificado para trabalhar com objetos Dish ...
```

### Integração com OrderBuilder
```python
# Modificações em order_builder.py
def add_item(self, item, quantity=1, customize=False):
    # ... código existente ...
    
    if customize:
        base_dish = self._order.restaurant.menu.get_dish(item)
        customized_dish = self._customize_dish(base_dish)
        # ... lógica para adicionar prato personalizado ...
```

### Exemplo de uso
```python
# Personalização de um prato
hamburguer = menu.get_dish("Hambúrguer")
hamburguer_personalizado = ExtraCheese(ExtraBacon(hamburguer))
print(hamburguer_personalizado.get_description())  # "Hambúrguer + bacon + queijo extra"
print(hamburguer_personalizado.get_price())  # Preço base + 4.50 + 3.00
```

### Benefícios Obtidos
1. **Flexibilidade**: Permite personalizar pratos sem modificar as classes existentes
2. **Composição dinâmica**: Extras podem ser adicionados em tempo de execução
3. **Princípio Open/Closed**: Novas personalizações podem ser adicionadas sem alterar o código existente
4. **Combinações ilimitadas**: Permite criar uma grande variedade de pratos personalizados
5. **Melhor experiência do cliente**: Oferece mais opções de personalização aos clientes

---

## Conclusão

A implementação destes padrões de design melhorou significativamente a arquitetura do sistema:

1. **Builder** (já existente) proporciona uma interface fluente para criação de pedidos
2. **Observer** permite notificações automáticas sobre mudanças de status da entrega
3. **Decorator** possibilita personalização de pratos com adição de extras e remoção de ingredientes

Juntos, estes padrões tornam o sistema mais flexível, modular e extensível, facilitando a adição de novas funcionalidades no futuro e melhorando a experiência do usuário.