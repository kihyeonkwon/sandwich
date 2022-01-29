from django.urls import path
from . import views


urlpatterns = [
    path('bread/', views.BreadView.as_view()),
    path('topping/', views.ToppingView.as_view()),
    path('cheese/', views.CheeseView.as_view()),
    path('sauce/', views.SauceView.as_view()),
    path('sandwich/', views.SandwichView.as_view()),
]
