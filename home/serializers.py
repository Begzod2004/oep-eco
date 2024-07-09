from rest_framework import serializers
from .models import ECOVolontyor, NewsCategory, News, Qabul, EDokon

class ECOVolontyorSerializer(serializers.ModelSerializer):
    class Meta:
        model = ECOVolontyor
        fields = '__all__'

class NewsCategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = NewsCategory
        fields = '__all__'

class NewsSerializer(serializers.ModelSerializer):
    category = NewsCategorySerializer()

    class Meta:
        model = News
        fields = '__all__'

class QabulSerializer(serializers.ModelSerializer):
    class Meta:
        model = Qabul
        fields = '__all__'

class EDokonSerializer(serializers.ModelSerializer):
    class Meta:
        model = EDokon
        fields = '__all__'
