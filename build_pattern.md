# Implementação do Padrão Builder

## Visão Geral

O padrão Builder foi implementado no projeto de sistema de delivery online para simplificar a criação de pedidos, que têm muitos componentes opcionais. Este padrão separa a construção de um objeto complexo (Order) da sua representação, permitindo criar diferentes representações usando o mesmo processo de construção.

## Motivação

A classe Order original exigia múltiplas chamadas de método para configurar completamente um pedido:

```python
# Abordagem anterior
order = Order(customer, restaurant)
order.add_item("Pizza", 2)
order.add_item("Refrigerante", 3)
order.set_delivery_instructions("Deixar na portaria")
order.set_delivery_time_preference("19:30")
order.set_payment_method(payment)
```

Esta abordagem apresentava algumas limitações:
- Verbosa e repetitiva
- Difícil de encadear operações
- Cliente precisa conhecer a sequência correta de chamadas
- Dificuldade em garantir que o objeto esteja em um estado válido antes de usá-lo

## Implementação

A implementação do padrão Builder para pedidos conta com:

### 1. OrderBuilder

Classe responsável por construir objetos Order incrementalmente com uma interface fluente:

```python
from order_builder import OrderBuilder

# Criação de pedido com Builder
order = OrderBuilder(customer, restaurant) \
    .add_item("Pizza", 2) \
    .add_item("Refrigerante", 3) \
    .with_delivery_instructions("Deixar na portaria") \
    .with_delivery_time("19:30") \
    .with_payment_method(payment) \
    .with_promo_code("DESCONTO10") \
    .build()
```

### 2. Principais características

- **Interface Fluente**: Cada método retorna `self`, permitindo encadeamento de chamadas
- **Validação Incremental**: Cada método pode validar seus parâmetros antes de prosseguir
- **Flexibilidade**: Parâmetros opcionais podem ser adicionados em qualquer ordem
- **Separação de Preocupações**: A lógica de construção fica isolada da lógica do produto
- **Reutilização**: O builder pode ser reutilizado para criar múltiplos pedidos

### 3. Métodos Implementados

| Método | Descrição |
|--------|-----------|
| `__init__(customer, restaurant)` | Inicializa o builder com parâmetros obrigatórios |
| `add_item(item, quantity)` | Adiciona um item ao pedido |
| `remove_item(item)` | Remove um item do pedido |
| `with_delivery_instructions(instructions)` | Define instruções de entrega |
| `with_delivery_time(time_preference)` | Define horário preferido |
| `with_payment_method(payment_method)` | Define método de pagamento |
| `with_promo_code(promo_code)` | Aplica código promocional |
| `build()` | Constrói e retorna o objeto Order finalizado |
| `reset()` | Reseta o builder para criar um novo pedido |

## Integração no Sistema

O sistema agora oferece duas formas de criar pedidos:
1. Método tradicional (passo a passo)
2. Usando o Builder (mais flexível e intuitivo)

A interface de linha de comando foi atualizada para acomodar ambas as abordagens, com o Builder oferecendo uma experiência mais guiada de criação de pedidos.

## Benefícios Obtidos

1. **Código mais legível e expressivo**
2. **Redução de erros na criação de objetos complexos**
3. **Maior flexibilidade na ordem de configuração**
4. **Verificação de consistência antes da criação do objeto final**
5. **Separação clara entre construção e representação**
6. **Demonstração prática de um padrão de design importante**

## Exemplos de Uso

### Exemplo Básico
```python
order = OrderBuilder(customer, restaurant) \
    .add_item("Pizza", 1) \
    .build()
```

### Exemplo Completo
```python
order = OrderBuilder(customer, restaurant) \
    .add_item("Pizza", 2) \
    .add_item("Refrigerante", 3) \
    .with_delivery_instructions("Prédio azul, apt 303") \
    .with_delivery_time("19:30") \
    .with_payment_method(CreditCard(amount, card_number, expiry, cvv)) \
    .with_promo_code("DESCONTO10") \
    .build()
```

### Criação de Múltiplos Pedidos
```python
builder = OrderBuilder(customer, restaurant)

# Primeiro pedido
order1 = builder \
    .add_item("Pizza", 1) \
    .build()

# Reseta e cria um segundo pedido
order2 = builder.reset() \
    .add_item("Hambúrguer", 2) \
    .build()
```