from menu import Menu
from review import Review
from promotion import Promotion


class Restaurant:
    def __init__(self, name, address, owner):
        self.name = name
        self.address = address
        self.owner = owner
        self.menu = Menu(self)
        self.reviews = Review()
        self.promotions = Promotion(self)

    def add_review(self, user, review_text, rating):
        """Adiciona uma avaliação."""
        if user.id == self.owner.id:
            raise PermissionError("O proprietário não pode avaliar o próprio restaurante.")
        # Passamos o usuário diretamente para o método add_review
        self.reviews.add_review(user, review_text, rating)

    def display_menu(self):
        """Exibe o menu."""
        return self.menu.display_menu()

    def display_promotions(self):
        """Exibe as promoções."""
        return self.promotions.display_promotions()

    def display_reviews(self):
        """Exibe as avaliações."""
        return self.reviews.display_reviews()

    def get_average_rating(self):
        """Retorna a média das avaliações."""
        return self.reviews.get_average_rating()