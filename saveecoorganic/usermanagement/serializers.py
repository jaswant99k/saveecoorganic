from pyexpat import model
from django.contrib.auth.models import User
from rest_framework import serializers
from .models import *
from django.contrib.auth.hashers import make_password
from django.db.models import Q
from django.contrib.auth.models import Group







class UserSerializer(serializers.ModelSerializer):
    #user_profile = serializers.SerializerMethodField()
    password = serializers.CharField(write_only=True,required=True,)
    #user = UserAccountSerializers(many=True)
    class Meta:
        model = User
        fields = ['password', 'email']


class UserAccountSerializers(serializers.ModelSerializer):
    email = serializers.EmailField(source='user.email')
    password = serializers.CharField(write_only=True,required=True,source='user.password')

    class Meta:
        model = UserAccount
        fields = ['name', 'mobile','referral','position','email', 'password' ]

    def create(self, validated_data):
        #user = UserSerializer(data=validated_data['user'])
        password = make_password(validated_data['user']['password'])
        user = User.objects.create(username=validated_data['user']['email'], password=password, email=validated_data['user']['email'])
        validated_data.pop("user")
        instance = UserAccount.objects.create(user=user, **validated_data) 
        try:
            add_group = Group.objects.get(name='member')
        except:
            add_group = Group.objects.create(name='member')

        instance.user.groups.add(add_group)
        return instance
        




