from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from suppliers.models import Supplier
import random


class Command(BaseCommand):
    help = "Generate Fake Suppliers"
    faker = Faker()

    def handle(self, *args, **kwargs):
        for i in range(1,101,1):
         Supplier.objects.create(
            name = self.faker.name(),
            contact_info = self.faker.phone_number(),
            address = self.faker.address(),
            is_active=random.choice([True, False])  
        
             
        )
         self.stdout.write(self.style.SUCCESS("100 supplier generated sucessfulluy"))