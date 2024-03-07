from rest_framework import serializers
from django.contrib.auth.models import User
from limonapp.models import Advertisement, Subcategory, AdvertiseStatus, Condition
import json


class AdvertisementSerializer(serializers.ModelSerializer):
    condition = serializers.PrimaryKeyRelatedField(queryset=Condition.objects.all(), required=False)
    subcategory = serializers.PrimaryKeyRelatedField(queryset=Subcategory.objects.all(), required=False)
    attributes = serializers.JSONField()
    user = serializers.HiddenField(default=serializers.CurrentUserDefault())

    class Meta:
        model = Advertisement
        fields = ('id', 'title', 'user', 'description', 'price', 'subcategory', 'condition', 'attributes', 'images')

    def get_subcategory(self, obj):
        subcategory = obj.category.subcategory_set.first()
        if subcategory:
            return subcategory.subcategory
        else:
            return None

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['attributes'] = instance.attributes
        return representation


# from rest_framework import serializers
# from django.contrib.auth.models import User


class UserSerializer(serializers.ModelSerializer):
    password = serializers.CharField(write_only=True)

    def create(self, validated_data):
        user = User.objects.create_user(**validated_data)
        return user

    class Meta:
        model = User
        fields = ['username', 'password']
