from django.core.management.base import BaseCommand
from faker import Faker
from products.models import Category, Product
import random


class Command(BaseCommand):
    help = 'Génère des données fictives pour les produits'

    def handle(self, *args, **options):
        faker = Faker('fr_FR')  # langue française

        # Supprimer anciennes données (optionnel mais propre)
        Product.objects.all().delete()
        Category.objects.all().delete()

        # créer 5 catégories
        categories = []

        for _ in range(5):
            name = faker.word().capitalize()
            slug = name.lower().replace(" ", "-")

            category = Category.objects.create(
                name=name,
                slug=slug
            )

            categories.append(category)
            self.stdout.write(self.style.SUCCESS(f'Catégorie créée: {name}'))

        # créer des produits
        for i in range(8):
            product = Product.objects.create(
                name=faker.sentence(nb_words=4).replace('.', ''),
                description=faker.text(max_nb_chars=450),
                price=round(random.uniform(10, 999), 2),
                stock=random.randint(0, 100),
                category=random.choice(categories)
            )

            self.stdout.write(self.style.SUCCESS(f'Produit {i+1} créé: {product.name}'))