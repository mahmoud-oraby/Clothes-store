from rest_framework import serializers
from .models import Product,Color, Size, Currency

class ColorSerializer(serializers.ModelSerializer):
    class Meta:
        model = Color
        fields = ['name','rgb']
        read_only_fields = ['id',]

class SizeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Size
        fields = ['name',]


class CurrencySerializer(serializers.ModelSerializer):
    class Meta:
        model = Currency
        fields = ['name','symbol']
        read_only_fields = ['id',]


class ProductSerializer(serializers.ModelSerializer):
    colors = ColorSerializer(many=True)
    currency = CurrencySerializer()
    size = serializers.SerializerMethodField()
    class Meta:
        model = Product
        fields = '__all__'
        read_only_fields = ['id']
    
    def get_size(self, obj):
        sizes = obj.size.all()
        return [size.name for size in sizes]
    
    def create(self, validated_data):
        # Extract the color data from the validated data
        color_data = validated_data.pop('colors', [])
        size_data = validated_data.pop('size', [])
        currency_data = validated_data.pop('size')

        currency = Currency.objects.get_or_create(**currency_data)

        product = Product.objects.create(currency=currency,**validated_data)

        for color in color_data:
            color_obj, created = Color.objects.get_or_create(**color)
            product.colors.add(color_obj)

        for size in size_data:
            size_obj, created = Size.objects.get_or_create(**size)
            product.colors.add(size_obj)


        return product
    
