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

def manage_orders(customers, restaurants, orders, deliveries):
    print("\n--- Gerenciar Pedidos ---")
    print("1. Criar Pedido (Método tradicional)")
    print("2. Criar Pedido (Método Builder)")
    print("3. Adicionar Item ao Pedido")
    print("4. Adicionar Instruções de Entrega")
    print("5. Definir Preferência de Horário")
    print("6. Aplicar código promocional")
    print("7. Exibir Pedido")
    print("8. Finalizar Pedido")
    print("9. Voltar")
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
        from order_builder import OrderBuilder

        customer_name = input("Nome do Cliente: ")
        customer = next((c for c in customers if c.name == customer_name), None)
        if customer:
            restaurant_name = input("Nome do Restaurante: ")
            restaurant = next((r for r in restaurants if r.name == restaurant_name), None)
            if restaurant:
                builder = OrderBuilder(customer, restaurant)

                adding_items = True
                while adding_items:
                    dish_name = input("Nome do Prato (ou deixe em branco para terminar): ")
                    if not dish_name:
                        adding_items = False
                        continue

                    try:
                        quantity = int(input("Quantidade: "))
                        builder.add_item(dish_name, quantity)
                        print(f'Item {dish_name} adicionado ao pedido.')
                    except ValueError as e:
                        print(f'Erro: {e}')

                instructions = input("Instruções de entrega (Opcional): ")
                if instructions:
                    builder.with_delivery_instructions(instructions)

                time_preference = input("Horário preferido para entrega (Opcional): ")
                if time_preference:
                    builder.with_delivery_time(time_preference)

                promo_code = input("Código promocional (Opcional): ")
                if promo_code:
                    builder.with_promo_code(promo_code)

                order = builder.build()
                orders.append(order)
                print("Pedido criado com sucesso usando Builder!")
                print(order.display_order())
            else:
                print("Restaurante não encontrado.")
        else:
            print("Cliente não encontrado.")
            
    elif choice == "3":
        customer_name = input("Nome do Cliente: ")
        order = next((o for o in orders if o.customer.name == customer_name), None)
        if order:
            dish_name = input("Nome do Prato: ")
            quantity = int(input("Quantidade: "))
            try:
                order.add_item(dish_name, quantity)
                print("Item adicionado ao pedido com sucesso!")
            except ValueError as e:
                print(f"Erro: {e}")
        else:
            print("Pedido não encontrado.")
            
    elif choice == "4":
        customer_name = input("Nome do Cliente: ")
        order = next((o for o in orders if o.customer.name == customer_name), None)
        if order:
            instructions = input("Instruções de entrega: ")
            order.set_delivery_instructions(instructions)
            print("Instruções de entrega adicionadas com sucesso!")
        else:
            print("Pedido não encontrado.")
            
    elif choice == "5":
        customer_name = input("Nome do Cliente: ")
        order = next((o for o in orders if o.customer.name == customer_name), None)
        if order:
            time_preference = input("Horário preferido para entrega (ex: 19:30): ")
            order.set_delivery_time_preference(time_preference)
            print("Preferência de horário definida com sucesso!")
        else:
            print("Pedido não encontrado.")
    
    elif choice == "6":
        customer_name = input("Nome do Cliente: ")
        order = next((o for o in orders if o.customer.name == customer_name), None)
        if order:
            promo_code = input("Código promocional: ")
            if order.apply_promo_code(promo_code):
                print("Código promocional aplicado com sucesso!")
            else:
                print("Código promocional inválido.")
        else:
            print("Pedido não encontrado.")
            
    elif choice == "7":
        customer_name = input("Nome do Cliente: ")
        order = next((o for o in orders if o.customer.name == customer_name), None)
        if order:
            print(order.display_order())
        else:
            print("Pedido não encontrado.")
            
    elif choice == "8":
        customer_name = input("Nome do Cliente: ")
        order = next((o for o in orders if o.customer.name == customer_name), None)
        if order:
            # Verifica se já existe uma entrega para este pedido
            existing_delivery = next((d for d in deliveries if d.order == order), None)
            if not existing_delivery:
                from delivery import Delivery
                delivery = Delivery(order)
                deliveries.append(delivery)
                # Utiliza o método finalize_order
                print(order.finalize_order(delivery))
                print("Entrega iniciada!")
                print(delivery.display_status())
            else:
                print("Este pedido já possui uma entrega em andamento.")
        else:
            print("Pedido não encontrado.")
            
    elif choice == "9":
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
    print("1. Rastrear entrega")
    print("2. Atualizar status da entrega")
    print("3. Simular progresso da entrega")
    print("4. Atribuir entregador")
    print("5. Atualizar localização")
    print("6. Adicionar nota de entrega")
    print("7. Voltar")
    choice = input("Escolha uma opção: ")

    if choice == "1":
        customer_name = input("Nome do Cliente: ")
        delivery = next((d for d in deliveries if d.order.customer.name == customer_name), None)
        if delivery:
            print(delivery.display_status())
        else:
            print("Entrega não encontrada.")
            
    elif choice == "2":
        customer_name = input("Nome do Cliente: ")
        delivery = next((d for d in deliveries if d.order.customer.name == customer_name), None)
        if delivery:
            print("Status disponíveis:")
            print("1. Em preparo")
            print("2. Pronto para entrega")
            print("3. Entregador designado")
            print("4. Pedido coletado")
            print("5. A caminho")
            print("6. Próximo ao destino")
            print("7. Chegou ao destino")
            print("8. Entregue")
            print("9. Cancelado")
            status_choice = input("Escolha o novo status: ")
            
            status_map = {
                "1": "Em preparo",
                "2": "Pronto para entrega",
                "3": "Entregador designado",
                "4": "Pedido coletado",
                "5": "A caminho",
                "6": "Próximo ao destino",
                "7": "Chegou ao destino",
                "8": "Entregue",
                "9": "Cancelado"
            }
            
            if status_choice in status_map:
                notes = input("Notas adicionais (opcional): ")
                delivery.update_status(status_map[status_choice], notes)
                print("Status da entrega atualizado com sucesso!")
            else:
                print("Opção inválida.")
        else:
            print("Entrega não encontrada.")
            
    elif choice == "3":
        customer_name = input("Nome do Cliente: ")
        delivery = next((d for d in deliveries if d.order.customer.name == customer_name), None)
        if delivery:
            delivery.simulate_delivery_progress()
            print("Progresso da entrega simulado com sucesso!")
            print(delivery.display_status())
        else:
            print("Entrega não encontrada.")
            
    elif choice == "4":
        customer_name = input("Nome do Cliente: ")
        delivery = next((d for d in deliveries if d.order.customer.name == customer_name), None)
        if delivery:
            delivery_person = input("Nome do entregador: ")
            delivery.assign_delivery_person(delivery_person)
            print(f"Entregador {delivery_person} designado com sucesso!")
        else:
            print("Entrega não encontrada.")
            
    elif choice == "5":
        customer_name = input("Nome do Cliente: ")
        delivery = next((d for d in deliveries if d.order.customer.name == customer_name), None)
        if delivery:
            try:
                latitude = float(input("Latitude: "))
                longitude = float(input("Longitude: "))
                delivery.update_location(latitude, longitude)
                print("Localização atualizada com sucesso!")
            except ValueError:
                print("Coordenadas inválidas. Use valores numéricos.")
        else:
            print("Entrega não encontrada.")
            
    elif choice == "6":
        customer_name = input("Nome do Cliente: ")
        delivery = next((d for d in deliveries if d.order.customer.name == customer_name), None)
        if delivery:
            note = input("Nota de entrega: ")
            delivery.add_delivery_note(note)
            print("Nota adicionada com sucesso!")
        else:
            print("Entrega não encontrada.")
            
    elif choice == "7":
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
            manage_orders(customers, restaurants, orders, deliveries)  # Adicionado deliveries como parâmetro

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
