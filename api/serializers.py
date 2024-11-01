from django.contrib.auth.models import Group, User
from rest_framework import serializers

from api.models import MyModel


# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:

# model = User
# # fields = ['first_name', 'last_name', 'email']
# fields = ['url', 'username', 'email', 'groups']


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ['url', 'name']


class MyModelSerializer(serializers.ModelSerializer):
    class Meta:
        model = MyModel
        fields = '__all__'
