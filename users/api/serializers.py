from users.models import Role,User
from rest_framework import serializers

class RoleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Role
        fields = '__all__'
 
class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name','email','password','role']

    def to_representation(self, instance):
        data =  super().to_representation(instance)            
        return data