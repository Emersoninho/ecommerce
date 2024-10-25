from django.urls import path
from e_commerce import views

urlpatterns = [
    path('', views.home_page, name='home_page'),
]
