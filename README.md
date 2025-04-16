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

8. **order_builder.py**: Implementa o padrão de design Builder para criação de pedidos de forma mais flexível e fluente.

9. **menu.py**: Implementa a classe `Menu`, que permite aos proprietários de restaurantes gerenciar os itens do menu e seus preços.

10. **delivery.py**: Implementa as classes `Delivery` e `DeliveryLocation` para rastreamento em tempo real de entregas, incluindo coordenadas geográficas, histórico de status e estimativas de tempo.

11. **permissions.py**: Implementa a classe `PermissionManager`, que centraliza a lógica de verificação de permissões em todo o sistema.

12. **analytics.py**: Implementa a classe `RestaurantAnalytics`, que fornece análises e métricas de desempenho para os restaurantes, incluindo geração de gráficos e dashboards.

13. **app.py**: Aplicação principal que integra todos os módulos e fornece uma interface de linha de comando para interação com o sistema.

## Conceitos de POO Implementados

Este projeto aplica diversos conceitos de Programação Orientada a Objetos:

1. **Classes e Objetos**: Todo o sistema é modelado usando classes que representam entidades do mundo real (Restaurantes, Menus, Pedidos, etc).

2. **Herança**: As classes `Customer` e `Owner` herdam da classe abstrata `User`. As classes de pagamento herdam da classe abstrata `Payment`.

3. **Encapsulamento**: Atributos privados são marcados com underscore (`_`) e acessados através de métodos específicos.

4. **Polimorfismo**: Diferentes implementações do método `process_payment()` nas subclasses de `Payment`.

5. **Classes Abstratas**: `User` e `Payment` são classes abstratas que definem interfaces para suas subclasses.

6. **Padrões de Design**: Implementação do padrão Builder para a criação de pedidos, permitindo uma construção mais flexível e legível.

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

### Rastreamento de Entregas em Tempo Real
- A classe `Delivery` implementa um sistema completo de rastreamento de entregas:
  - **Status detalhados**: Rastreamento granular com 9 diferentes status (Em preparo, Pronto para entrega, Entregador designado, Pedido coletado, A caminho, Próximo ao destino, Chegou ao destino, Entregue, Cancelado)
  - **Localização geográfica**: Coordenadas de latitude e longitude do entregador
  - **Tempo estimado de entrega**: Cálculo dinâmico do tempo restante para entrega
  - **Histórico completo**: Registro detalhado de todas as mudanças de status com timestamp
  - **Atribuição de entregador**: Associação de um entregador específico a cada pedido
  - **Notas de entrega**: Possibilidade de adicionar informações relevantes durante o processo
  - **Simulação**: Funcionalidade para simular o progresso da entrega em tempo real

### Gerenciamento de Permissões
- O sistema utiliza a classe `PermissionManager` para verificar permissões de forma consistente em todo o código.

## Como Usar

Para executar o projeto e mostrar as funcionalidades, use:

```bash
python app.py
```

### Fluxo básico de uso:

1. Cadastre-se como Cliente ou Proprietário de Restaurante
2. (Para Proprietários) Adicione restaurantes e configure seus menus
3. (Para Clientes) Faça pedidos escolhendo pratos do menu
4. Adicione instruções de entrega e preferências de horário aos pedidos
5. Finalize o pedido para iniciar o processo de entrega
6. Acompanhe o status da entrega em tempo real
7. Simule o progresso da entrega para testes
8. Avalie o restaurante após receber o pedido

### Testando o sistema de rastreamento:

Para testar o sistema de rastreamento de entregas em tempo real:
1. Acesse "Gerenciar Entregas" no menu principal
2. Utilize a opção "Simular progresso da entrega" repetidamente para ver o ciclo completo
3. Acompanhe as mudanças de status, coordenadas geográficas e estimativas de tempo

## Melhorias Implementadas

- Eliminação de importações circulares
- Centralização de verificações de permissão com a classe `PermissionManager`
- Encapsulamento apropriado de atributos protegidos
- Adição de opções de entrega personalizáveis
- Melhor consistência no design de classes
- Implementação de um sistema robusto de rastreamento de entregas em tempo real
- Simulação para testes e demonstrações do sistema
- Histórico completo de status para pedidos e entregas
- Interface aprimorada para gerenciamento de entregas
- Sistema completo de analytics para restaurantes
- Implementação do padrão de design Builder para criação flexível de pedidos
- Integração de códigos promocionais aos pedidos