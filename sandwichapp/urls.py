from django.urls import path, include
from . import views
from .views import BreadViewSet, ToppingViewSet, CheeseViewSet, SauceViewSet, SandwichViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()

router.register('bread', BreadViewSet)
router.register('topping', ToppingViewSet)
router.register('cheese', CheeseViewSet)
router.register('sauce', SauceViewSet)
router.register('sandwich', SandwichViewSet)


urlpatterns = [
    path('', include(router.urls)),
]
