from django.core.management.base import BaseCommand
from faker import Faker
from users.models import Role, User 
import random

class Command(BaseCommand):
    help = "Generate Fake Role and User data"
    
    def handle(self, *args, **kwargs):
        fake = Faker()
        
        
        roles = []
        for role_choice in Role.RoleChoices:
            role = Role.objects.create(
                role_name=role_choice[0],
                description=fake.sentence()
            )
            roles.append(role)
        
        self.stdout.write(self.style.SUCCESS(f"Created {len(roles)} roles."))
        
    
        for _ in range(100):  
            user = User.objects.create(
                name=fake.name(),
                email=fake.email(),
                password=fake.password(),  
                role=random.choice(roles) 
            )
        
        self.stdout.write(self.style.SUCCESS("Successfully generated 100 users."))
