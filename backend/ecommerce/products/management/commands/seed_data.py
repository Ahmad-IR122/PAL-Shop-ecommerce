from django.core.management.base import BaseCommand
from products.models import Product
from products.models import Category

class Command(BaseCommand):
    help = "Seed products data"

    def handle(self, *args, **kwargs):
        categories = {
            "Electronics": [
                {
                    "name": "Wireless Headphones",
                    "slug": "wireless-headphones",
                    "description": "Bluetooth wireless headphones with noise cancellation",
                    "price": 99.99,
                    "stock": 40,
                    "image": "products/headphones.jpg"
                },
                {
                    "name": "Smart Watch",
                    "slug": "smart-watch",
                    "description": "Fitness smart watch with heart rate monitor",
                    "price": 149.99,
                    "stock": 25,
                    "image": "products/smartwatch.jpg"
                }
            ],
            "Beauty & Personal Care": [
                {
                    "name": "Face Cleanser",
                    "slug": "face-cleanser",
                    "description": "Gentle face cleanser for daily use",
                    "price": 14.99,
                    "stock": 60,
                    "image": "products/face_cleanser.jpg"
                }
            ],
            "Books": [
                {
                    "name": "Python Programming Book",
                    "slug": "python-programming-book",
                    "description": "Learn Python from beginner to advanced",
                    "price": 29.99,
                    "stock": 35,
                    "image": "products/python_book.jpg"
                }
            ],
            "Toys & Baby Products": [
                {
                    "name": "Baby Toy Set",
                    "slug": "baby-toy-set",
                    "description": "Safe and colorful toy set for babies",
                    "price": 19.99,
                    "stock": 50,
                    "image": "products/baby_toys.jpg"
                }
            ],
            "Sports & Fitness": [
                {
                    "name": "Yoga Mat",
                    "slug": "yoga-mat",
                    "description": "Non-slip yoga mat",
                    "price": 24.99,
                    "stock": 45,
                    "image": "products/yoga_mat.jpg"
                }
            ],
            "Tools & Hardware": [
                {
                    "name": "Electric Drill",
                    "slug": "electric-drill",
                    "description": "High power electric drill",
                    "price": 89.99,
                    "stock": 20,
                    "image": "products/drill.jpg"
                }
            ],
            "Pet Supplies": [
                {
                    "name": "Dog Food",
                    "slug": "dog-food",
                    "description": "Healthy dog food 5kg",
                    "price": 34.99,
                    "stock": 30,
                    "image": "products/dog_food.jpg"
                }
            ],
            "Grocery & Food": [
                {
                    "name": "Organic Honey",
                    "slug": "organic-honey",
                    "description": "100% organic natural honey",
                    "price": 12.99,
                    "stock": 70,
                    "image": "products/honey.jpg"
                }
            ],
            "Fashion & Apparel": [
                {
                    "name": "Men T-Shirt",
                    "slug": "men-t-shirt",
                    "description": "Cotton men t-shirt",
                    "price": 19.99,
                    "stock": 55,
                    "image": "products/tshirt.jpg"
                }
            ]
        }

        created_count = 0

        for category_name, products in categories.items():
            try:
                category = Category.objects.get(name=category_name)
            except Category.DoesNotExist:
                self.stdout.write(
                    self.style.WARNING(f"Category '{category_name}' not found, skipping...")
                )
                continue

            for product_data in products:
                product, created = Product.objects.get_or_create(
                    slug=product_data["slug"],
                    defaults={
                        "category": category,
                        "name": product_data["name"],
                        "description": product_data["description"],
                        "price": product_data["price"],
                        "stock": product_data["stock"],
                        "image": product_data["image"],
                        "is_active": True
                    }
                )
                if created:
                    created_count += 1

        self.stdout.write(
            self.style.SUCCESS(f"✅ Successfully seeded {created_count} products")
        )
