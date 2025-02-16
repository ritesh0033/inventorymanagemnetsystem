from django.core.management.base import BaseCommand
from faker import Faker
from product.models import Category, Product
import random  

class Command(BaseCommand): 
    help = "Generate Fake category and product"
    
    def handle(self, *args, **kwargs):
        fake = Faker()
        categories = []
        
        
        for _ in range(100):  
            category = Category.objects.create(
                name=fake.word().capitalize(),  
                description=fake.sentence()
            )
            categories.append(category)  
        self.stdout.write(self.style.SUCCESS(f"Created {len(categories)} categories."))
      
        
        for _ in range(100):
            product = Product.objects.create(
                name=fake.word().capitalize(),  
                description=fake.sentence(),
                category=random.choice(categories),  
                price=round(random.uniform(10, 5000), 2),  
                stock_quantity=random.randint(1, 500),  
                reorder_level=random.randint(1, 100)  
            )
       
        self.stdout.write(self.style.SUCCESS("Successfully generated 100 products."))
