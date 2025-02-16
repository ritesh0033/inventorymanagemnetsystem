from django.core.management.base import BaseCommand
from faker import Faker
from customers.models import Customer

class Command(BaseCommand):
    help = "Generate fake customer data"
    
    def handle(self, *args, **kwargs):
        fake = Faker()

        for _ in range(100): 
            Customer.objects.create(
                name=fake.name(),
                contact_info=fake.phone_number(),  
                address=fake.address()
            )

        self.stdout.write(self.style.SUCCESS("Successfully generated 100 customers."))
