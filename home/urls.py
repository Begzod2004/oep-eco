from django.urls import include, path
from rest_framework.routers import DefaultRouter
from .views import ECOVolontyorViewSet, NewsCategoryViewSet, NewsViewSet, QabulViewSet, EDokonViewSet

router = DefaultRouter()
router.register(r'ecovolontyors', ECOVolontyorViewSet)
router.register(r'newscategories', NewsCategoryViewSet)
router.register(r'news', NewsViewSet)
router.register(r'qabul', QabulViewSet)
router.register(r'edokon', EDokonViewSet)

urlpatterns = [
    path('', include(router.urls)),
]
