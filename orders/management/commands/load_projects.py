from django.core.management.base import BaseCommand
from django.utils import timezone
from faker import Faker
from orders.models import Order
from customers.models import Customer 

class Command(BaseCommand):
    help = "Generate fake orders"
    fake = Faker()

    def handle(self, *args, **kwargs):
        customers = Customer.objects.all()
        if not customers:
            self.stdout.write(self.style.ERROR("No customers found. Add customers first."))
            return
        
        for _ in range(100):  
            customer = self.fake.random_element(customers)
            Order.objects.create(
                customer=customer,
                order_date=self.fake.date_between(start_date="-1y", end_date="today"),
                status=self.fake.random_element([choice for choice, _ in Order.OrderStatus.choices])
            )
        
        self.stdout.write(self.style.SUCCESS("Successfully generated 100 orders."))


