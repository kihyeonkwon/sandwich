from django.urls import path
from . import views


urlpatterns = [
    path('bread/', views.BreadView.as_view()),
    # path('topping/', views.Topping.as_view()),
    # path('cheese/', views.Cheese.as_view()),
    # path('sauce/', views.Sauce.as_view()),
    # path('sandwich/', views.Sandwich.as_view()),
]
