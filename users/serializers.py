from rest_framework import serializers
from .models import CustomUser

class UserRegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ('username', 'password', 'nickname', 'age')
        extra_kwargs = {'password' : {'write_only' : True}}
def create(self, validated_data):

    user = CustomUser(
        username = validated_data['username'],
        nickname = validated_data.get('nickname'),
        age = validated_data.get('age'),
    )

    user.set_password(validated_data['password'])
    user.save()
    return user