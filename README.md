# Online Food Delivery Service

Este projeto é um sistema de delivery de comida online desenvolvido como parte da disciplina de Projeto de Software na Universidade Federal de Alagoas (UFAL), ministrada pelo Professor Dr. Baldoíno Fonseca dos Santos Neto.

## Estrutura do Projeto

O projeto consiste nos seguintes módulos:

1. **users.py**: Contém as classes `User` (abstrata), `Customer` e `Owner`. Essas classes representam os usuários do sistema, com `Customer` e `Owner` sendo subclasses da classe abstrata `User`.

2. **support.py**: Implementa a classe `Support`, que gerencia tickets de suporte aos clientes.

3. **review.py**: Implementa a classe `Review`, que permite aos clientes adicionar, atualizar e excluir avaliações para restaurantes.

4. **restaurant.py**: Implementa a classe `Restaurant`, que representa um restaurante e inclui funcionalidades para gerenciar menus, avaliações e promoções.

5. **promotion.py**: Implementa a classe `Promotion`, que permite aos proprietários de restaurantes gerenciar promoções e descontos.

6. **payment.py**: Implementa a classe abstrata `Payment` e suas subclasses (`CreditCard`, `DebitCard`, `Pix` e `Cash`) para lidar com diferentes métodos de pagamento.

7. **order.py**: Implementa a classe `Order`, que representa um pedido feito por um cliente em um restaurante. Inclui opções de entrega personalizáveis.

8. **menu.py**: Implementa a classe `Menu`, que permite aos proprietários de restaurantes gerenciar os itens do menu e seus preços.

9. **delivery.py**: Implementa a classe `Delivery`, que rastreia o status da entrega de um pedido.

10. **permissions.py**: Implementa a classe `PermissionManager`, que centraliza a lógica de verificação de permissões em todo o sistema.

## Conceitos de POO Implementados

Este projeto aplica diversos conceitos de Programação Orientada a Objetos:

1. **Classes e Objetos**: Todo o sistema é modelado usando classes que representam entidades do mundo real (Restaurantes, Menus, Pedidos, etc).

2. **Herança**: As classes `Customer` e `Owner` herdam da classe abstrata `User`. As classes de pagamento herdam da classe abstrata `Payment`.

3. **Encapsulamento**: Atributos privados são marcados com underscore (`_`) e acessados através de métodos específicos.

4. **Polimorfismo**: Diferentes implementações do método `process_payment()` nas subclasses de `Payment`.

5. **Classes Abstratas**: `User` e `Payment` são classes abstratas que definem interfaces para suas subclasses.

## Funcionalidades

### Usuários
- **Cliente**: Um cliente pode fazer pedidos, adicionar restaurantes favoritos e gerenciar seus métodos de pagamento.
- **Proprietário**: Um proprietário pode gerenciar seus restaurantes, adicionar/atualizar/remover itens do menu e gerenciar promoções.

### Suporte
- A classe `Support` permite que os clientes abram tickets de suporte e recebam respostas.

### Avaliações
- Os clientes podem adicionar, atualizar e excluir avaliações para restaurantes. O sistema calcula a avaliação média para cada restaurante.

### Restaurantes
- A classe `Restaurant` gerencia o menu, avaliações e promoções do restaurante. Os proprietários podem adicionar/atualizar/remover pratos e promoções.

### Pagamentos
- O sistema suporta múltiplos métodos de pagamento, incluindo cartão de crédito, cartão de débito, Pix e dinheiro. Cada método de pagamento valida os detalhes necessários antes de processar o pagamento.

### Pedidos
- Os clientes podem fazer pedidos adicionando itens do menu do restaurante. O sistema calcula o custo total do pedido.
- Os pedidos incluem opções de entrega personalizáveis, como instruções especiais e horário preferido.

### Menu
- A classe `Menu` permite aos proprietários de restaurantes gerenciar os pratos e seus preços.

### Entrega
- A classe `Delivery` rastreia o status da entrega de um pedido, incluindo atualizações sobre preparação, despacho e entrega.

### Gerenciamento de Permissões
- O sistema utiliza a classe `PermissionManager` para verificar permissões de forma consistente em todo o código.

## Como Usar

Para executar o projeto e mostrar as funcionalidades, use:

```bash
python app.py
```

## Melhorias Implementadas

- Eliminação de importações circulares
- Centralização de verificações de permissão
- Encapsulamento apropriado de atributos protegidos
- Adição de opções de entrega personalizáveis
- Melhor consistência no design de classes