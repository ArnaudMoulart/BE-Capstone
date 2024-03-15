from rest_framework import serializers
from django.contrib.auth.models import User, Group

from .models import Menu, Booking

class menuSerializer(serializers.ModelSerializer):
    class Meta:
        model = Menu
        fields = ['id','Title','Price','Inventory']

class bookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = '__all__'

class userSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['url', 'username', 'email', 'groups']

# class GroupNameField(serializers.RelatedField):
#     def to_representation(self, value):
#         # Return the group name
#         return value.name

# class UserSerializer(serializers.ModelSerializer):
#     groups = GroupNameField(many=True, read_only=True)
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')