from rest_framework import viewsets
from .models import ECOVolontyor, NewsCategory, News, Qabul, EDokon
from .serializers import ECOVolontyorSerializer, NewsCategorySerializer, NewsSerializer, QabulSerializer, EDokonSerializer

class ECOVolontyorViewSet(viewsets.ModelViewSet):
    queryset = ECOVolontyor.objects.all()
    serializer_class = ECOVolontyorSerializer

class NewsCategoryViewSet(viewsets.ModelViewSet):
    queryset = NewsCategory.objects.all()
    serializer_class = NewsCategorySerializer

class NewsViewSet(viewsets.ModelViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer

class QabulViewSet(viewsets.ModelViewSet):
    queryset = Qabul.objects.all()
    serializer_class = QabulSerializer

class EDokonViewSet(viewsets.ModelViewSet):
    queryset = EDokon.objects.all()
    serializer_class = EDokonSerializer
