# OFDS-v3
 
# Online Food Delivery Service

This project is an online food delivery system developed as part of the Software Project course at the Federal University of Alagoas (Universidade Federal de Alagoas - UFAL), taught by Professor Dr. Baldoíno Fonseca dos Santos Neto.

## Project Structure

The project consists of the following modules:

1. **users.py**: Contains the `User`, `Customer`, and `Owner` classes. These classes represent the users of the system, with `Customer` and `Owner` being subclasses of the abstract `User` class.

2. **support.py**: Implements the `Support` class, which handles customer support tickets.

3. **review.py**: Implements the `Review` class, which allows customers to add, update, and delete reviews for restaurants.

4. **restaurant.py**: Implements the `Restaurant` class, which represents a restaurant and includes functionality for managing menus, reviews, and promotions.

5. **promotion.py**: Implements the `Promotion` class, which allows restaurant owners to manage promotions and discounts.

6. **payment.py**: Implements the `Payment` abstract class and its subclasses (`CreditCard`, `DebitCard`, `Pix`, and `Cash`) for handling different payment methods.

7. **order.py**: Implements the `Order` class, which represents an order placed by a customer at a restaurant.

8. **menu.py**: Implements the `Menu` class, which allows restaurant owners to manage the menu items and their prices.

9. **delivery.py**: Implements the `Delivery` class, which tracks the status of an order's delivery.

## How to Use

### Users
- **Customer**: A customer can place orders, add favorite restaurants, and manage their payment methods.
- **Owner**: An owner can manage their restaurants, add/update/remove menu items, and manage promotions.

### Support
- The `Support` class allows customers to open support tickets and receive responses.

### Reviews
- Customers can add, update, and delete reviews for restaurants. The system calculates the average rating for each restaurant.

### Restaurants
- The `Restaurant` class manages the restaurant's menu, reviews, and promotions. Owners can add/update/remove dishes and promotions.

### Payments
- The system supports multiple payment methods, including credit card, debit card, Pix, and cash. Each payment method validates the necessary details before processing the payment.

### Orders
- Customers can place orders by adding items from the restaurant's menu. The system calculates the total cost of the order.

### Menu
- The `Menu` class allows restaurant owners to manage the dishes and their prices.

### Delivery
- The `Delivery` class tracks the status of an order's delivery, including updates on preparation, dispatch, and delivery.

To run the project and show the features use python app.py