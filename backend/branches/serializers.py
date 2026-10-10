from rest_framework import serializers
from .models import Company


class CompanySerializer(serializers.ModelSerializer):
    image_url     = serializers.ReadOnlyField()
    product_count = serializers.SerializerMethodField()

    class Meta:
        model  = Company
        fields = [
            'id', 'company_id', 'name', 'image', 'image_url',
            'details', 'address', 'contact_number', 'toll_free_number',
            'is_active', 'product_count', 'created_at',
        ]
        read_only_fields = ['id', 'created_at']

    def get_product_count(self, obj):
        return obj.products.filter(is_active=True).count()
