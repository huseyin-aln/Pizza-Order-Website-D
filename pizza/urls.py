from django.urls import path
from .views import home, order, pizzas, edit_order


urlpatterns = [
    path('', home, name='home'),
    path('order/', order, name='order'),
    path('pizzas/', pizzas, name='pizzas'),
    path('order/<int:pk>', edit_order, name='edit_order'),
]
