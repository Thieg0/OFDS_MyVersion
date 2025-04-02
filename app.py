import uuid  # Para gerar IDs únicos automaticamente
from users import Customer, Owner
from support import Support
from review import Review
from restaurant import Restaurant
from promotion import Promotion
from payment import CreditCard, DebitCard, Pix, Cash
from order import Order
from menu import Menu
from delivery import Delivery

def main_menu():
    print("\n--- Menu Principal ---")
    print("1. Cadastro e Login")
    print("2. Gerenciar Restaurantes")
    print("3. Gerenciar Pedidos")
    print("4. Gerenciar Avaliações")
    print("5. Gerenciar Promoções")
    print("6. Gerenciar Pagamentos")
    print("7. Gerenciar Suporte")
    print("8. Gerenciar Entregas")
    print("9. Sair")
    choice = input("Escolha uma opção: ")
    return choice

def register_and_login(customers, owners):
    print("\n--- Cadastro e Login ---")
    print("1. Cadastrar")
    print("2. Login")
    print("3. Voltar")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        user_type = input("Escolha o tipo de usuário (1 - Cliente, 2 - Dono de Restaurante): ")
        name = input("Nome: ")
        email = input("Email: ")
        phone = input("Telefone: ")
        password1 = input("Senha: ")
        password2 = input("Confirme a Senha: ")

        if password1 != password2:
            print("As senhas não coincidem. Tente novamente.")
            return None

        id = str(uuid.uuid4())  # Gera um ID único automaticamente

        if user_type == "1":
            customer = Customer(id, name, email, phone, password1)
            customers.append(customer)
            print("Cliente cadastrado com sucesso!")
        elif user_type == "2":
            owner = Owner(id, name, email, phone, password1)
            owners.append(owner)
            print("Dono de Restaurante cadastrado com sucesso!")
        else:
            print("Tipo de usuário inválido.")

    elif choice == "2":
        email = input("Email: ")
        password = input("Senha: ")

        # Verifica se é um cliente
        customer = next((c for c in customers if c.email == email and c.get_password() == password), None)
        if customer:
            print(f"Login bem-sucedido como Cliente: {customer.name}")
            return customer

        # Verifica se é um dono de restaurante
        owner = next((o for o in owners if o.email == email and o.get_password() == password), None)
        if owner:
            print(f"Login bem-sucedido como Dono de Restaurante: {owner.name}")
            return owner

        print("Email ou senha incorretos.")

    elif choice == "3":
        return None

    else:
        print("Opção inválida. Tente novamente.")

def manage_restaurants(owners, restaurants):
    print("\n--- Gerenciar Restaurantes ---")
    print("1. Adicionar Restaurante")
    print("2. Adicionar Prato ao Menu")
    print("3. Exibir Menu")
    print("4. Voltar")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        name = input("Nome do Restaurante: ")
        address = input("Endereço do Restaurante: ")
        owner_name = input("Nome do Proprietário: ")  
        owner = next((o for o in owners if o.name == owner_name), None)  
        if owner:
            restaurant = Restaurant(name, address, owner)
            restaurants.append(restaurant)
            print("Restaurante criado com sucesso!")
        else:
            print("Proprietário não encontrado.")
    elif choice == "2":
        restaurant_name = input("Nome do Restaurante: ")
        restaurant = next((r for r in restaurants if r.name == restaurant_name), None)
        if restaurant:
            dish_name = input("Nome do Prato: ")
            price = float(input("Preço do Prato: "))
            restaurant.menu.add_dish(restaurant.owner, dish_name, price)
            print("Prato adicionado com sucesso!")
        else:
            print("Restaurante não encontrado.")
    elif choice == "3":
        restaurant_name = input("Nome do Restaurante: ")
        restaurant = next((r for r in restaurants if r.name == restaurant_name), None)
        if restaurant:
            print(restaurant.display_menu())
        else:
            print("Restaurante não encontrado.")
    elif choice == "4":
        pass  # Voltar ao menu principal
    else:
        print("Opção inválida. Tente novamente.")

def manage_orders(customers, restaurants, orders):
    print("\n--- Gerenciar Pedidos ---")
    print("1. Criar Pedido")
    print("2. Adicionar Item ao Pedido")
    print("3. Exibir Pedido")
    print("4. Voltar")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        customer_name = input("Nome do Cliente: ") 
        customer = next((c for c in customers if c.name == customer_name), None)
        if customer:
            restaurant_name = input("Nome do Restaurante: ")
            restaurant = next((r for r in restaurants if r.name == restaurant_name), None)
            if restaurant:
                order = Order(customer, restaurant)
                orders.append(order)
                print("Pedido criado com sucesso!")
            else:
                print("Restaurante não encontrado.")
        else:
            print("Cliente não encontrado.")
    elif choice == "2":
        customer_name = input("Nome do Cliente: ")
        order = next((o for o in orders if o.customer.name == customer_name), None)
        if order:
            dish_name = input("Nome do Prato: ")
            quantity = int(input("Quantidade: "))
            order.add_item(dish_name, quantity)
            print("Item adicionado ao pedido com sucesso!")
        else:
            print("Pedido não encontrado.")
    elif choice == "3":
        customer_name = input("Nome do Cliente: ")
        order = next((o for o in orders if o.customer.name == customer_name), None)
        if order:
            print(order.display_order())
        else:
            print("Pedido não encontrado.")
    elif choice == "4":
        pass
    else:
        print("Opção inválida. Tente novamente.")

def manage_reviews(customers, restaurants):
    print("\n--- Gerenciar Avaliações ---")
    print("1. Adicionar Avaliação")
    print("2. Exibir Avaliações")
    print("3. Voltar")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        customer_name = input("Nome do Cliente: ")  
        customer = next((c for c in customers if c.name == customer_name), None) 
        if customer:
            restaurant_name = input("Nome do Restaurante: ")
            restaurant = next((r for r in restaurants if r.name == restaurant_name), None)
            if restaurant:
                review_text = input("Texto da Avaliação: ")
                rating = float(input("Nota (0-5): "))
                restaurant.add_review(customer, review_text, rating)
                print("Avaliação adicionada com sucesso!")
            else:
                print("Restaurante não encontrado.")
        else:
            print("Cliente não encontrado.")
    elif choice == "2":
        restaurant_name = input("Nome do Restaurante: ")
        restaurant = next((r for r in restaurants if r.name == restaurant_name), None)
        if restaurant:
            print(restaurant.display_reviews())
        else:
            print("Restaurante não encontrado.")
    elif choice == "3":
        pass
    else:
        print("Opção inválida. Tente novamente.")

def manage_promotions(owners, restaurants):
    print("\n--- Gerenciar Promoções ---")
    print("1. Adicionar Promoção")
    print("2. Exibir Promoções")
    print("3. Voltar")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        owner_name = input("Nome do Proprietário: ")
        owner = next((o for o in owners if o.name == owner_name), None)
        if owner:
            restaurant_name = input("Nome do Restaurante: ")
            restaurant = next((r for r in restaurants if r.name == restaurant_name), None)
            if restaurant:
                code = input("Código da Promoção: ")
                value = float(input("Valor da Promoção (0-1): "))
                restaurant.promotions.add_promotion(owner, code, value)
                print("Promoção adicionada com sucesso!")
            else:
                print("Restaurante não encontrado.")
        else:
            print("Proprietário não encontrado.")
    elif choice == "2":
        restaurant_name = input("Nome do Restaurante: ")
        restaurant = next((r for r in restaurants if r.name == restaurant_name), None)
        if restaurant:
            print(restaurant.display_promotions())
        else:
            print("Restaurante não encontrado.")
    elif choice == "3":
        pass
    else:
        print("Opção inválida. Tente novamente.")

def manage_payments():
    print("\n--- Gerenciar Pagamentos ---")
    print("1. Realizar Pagamento com Cartão de Crédito")
    print("2. Realizar Pagamento com Cartão de Débito")
    print("3. Realizar Pagamento com Pix")
    print("4. Realizar Pagamento em Dinheiro")
    print("5. Voltar")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        amount = float(input("Valor do Pagamento: "))
        card_number = input("Número do Cartão: ")
        expiration_date = input("Data de Expiração (MM/AA): ")
        cvv = input("CVV: ")
        payment = CreditCard(amount, card_number, expiration_date, cvv)
        print(payment.process_payment())
    elif choice == "2":
        amount = float(input("Valor do Pagamento: "))
        card_number = input("Número do Cartão: ")
        expiration_date = input("Data de Expiração (MM/AA): ")
        cvv = input("CVV: ")
        payment = DebitCard(amount, card_number, expiration_date, cvv)
        print(payment.process_payment())
    elif choice == "3":
        amount = float(input("Valor do Pagamento: "))
        payment = Pix(amount)
        print(payment.process_payment())
    elif choice == "4":
        amount = float(input("Valor do Pagamento: "))
        payment = Cash(amount)
        print(payment.process_payment())
    elif choice == "5":
        pass
    else:
        print("Opção inválida. Tente novamente.")

def manage_support(support, customers):
    print("\n--- Gerenciar Suporte ---")
    print("1. Abrir Ticket")
    print("2. Responder Ticket")
    print("3. Exibir Tickets")
    print("4. Voltar")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        customer_name = input("Nome do Cliente: ") 
        customer = next((c for c in customers if c.name == customer_name), None)  
        if customer:
            issue = input("Descreva o problema: ")
            print(support.open_ticket(customer.name, issue))  
        else:
            print("Cliente não encontrado.")
    elif choice == "2":
        ticket_index = int(input("Índice do Ticket: "))
        response = input("Resposta: ")
        print(support.respond_to_ticket(ticket_index, response))
    elif choice == "3":
        print(support.display_tickets())
    elif choice == "4":
        pass 
    else:
        print("Opção inválida. Tente novamente.")

def manage_deliveries(orders, deliveries):
    print("\n--- Gerenciar Entregas ---")
    print("1. Atualizar Status da Entrega")
    print("2. Exibir Status da Entrega")
    print("3. Voltar")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        customer_name = input("Nome do Cliente: ")  # Solicita o nome do cliente
        order = next((o for o in orders if o.customer.name == customer_name), None)  # Busca o pedido pelo nome do cliente
        if order:
            new_status = input("Novo Status: ")
            delivery = Delivery(order)
            delivery.update_status(new_status)
            deliveries.append(delivery)
            print("Status da entrega atualizado com sucesso!")
        else:
            print("Pedido não encontrado.")
    elif choice == "2":
        customer_name = input("Nome do Cliente: ")  # Solicita o nome do cliente
        delivery = next((d for d in deliveries if d.order.customer.name == customer_name), None)  # Busca a entrega pelo nome do cliente
        if delivery:
            print(delivery.display_status())
        else:
            print("Entrega não encontrada.")
    elif choice == "3":
        pass  # Voltar ao menu principal
    else:
        print("Opção inválida. Tente novamente.")

def main():
    customers = []
    owners = []
    restaurants = []
    orders = []
    support = Support()
    deliveries = []

    while True:
        choice = main_menu()

        if choice == "1":
            user = register_and_login(customers, owners)
            if user:
                print(f"Bem-vindo, {user.name}!")
                # Aqui você pode adicionar lógica para o menu do usuário logado

        elif choice == "2":
            manage_restaurants(owners, restaurants)

        elif choice == "3":
            manage_orders(customers, restaurants, orders)

        elif choice == "4":
            manage_reviews(customers, restaurants)

        elif choice == "5":
            manage_promotions(owners, restaurants)

        elif choice == "6":
            manage_payments()

        elif choice == "7":
            manage_support(support, customers)

        elif choice == "8":
            manage_deliveries(orders, deliveries)

        elif choice == "9":
            print("Saindo...")
            break

        else:
            print("Opção inválida. Tente novamente.")

if __name__ == "__main__":
    main()
