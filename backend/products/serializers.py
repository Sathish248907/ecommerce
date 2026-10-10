from rest_framework import serializers
from .models import Product
from branches.serializers import CompanySerializer


class ProductSerializer(serializers.ModelSerializer):
    discounted_price = serializers.ReadOnlyField()
    image_url        = serializers.ReadOnlyField()
    company_detail   = CompanySerializer(source='company', read_only=True)

    class Meta:
        model  = Product
        fields = [
            'id', 'product_id', 'name', 'type', 'image', 'image_url',
            'details', 'price', 'discount', 'discounted_price',
            'stock', 'company', 'company_detail', 'is_active',
            'created_at', 'updated_at',
        ]
        read_only_fields = ['id', 'created_at', 'updated_at']


class ProductListSerializer(serializers.ModelSerializer):
    discounted_price = serializers.ReadOnlyField()
    image_url        = serializers.ReadOnlyField()
    company_name     = serializers.CharField(source='company.name', read_only=True)

    class Meta:
        model  = Product
        fields = [
            'id', 'product_id', 'name', 'type', 'image_url',
            'price', 'discount', 'discounted_price',
            'stock', 'company_name', 'is_active', 'created_at',
        ]
