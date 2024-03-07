from rest_framework import serializers

from limonapp.models import Advertisement, Category, Subcategory


class AdvertisementSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source='user.username', read_only=True)
    condition = serializers.CharField(source='condition.condition', read_only=True)

    class Meta:
        model = Advertisement
        fields = (
            'id', 'title', 'description', 'price', 'start_date', 'user', 'subcategory', 'condition', 'attributes',
            'images')

    def get_subcategory(self, obj):
        subcategory = obj.subcategory.subcategory_set.first()
        if subcategory:
            return subcategory.subcategory
        else:
            return None
