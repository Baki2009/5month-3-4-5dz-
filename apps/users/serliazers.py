from rest_framework import serializers

from apps.users.models import User

class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('id', 'username', 
                  'age', 'email', 'phone', 'created_at')
