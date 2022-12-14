from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('group_list/', views.group_list, name='group_list'),
    path('cats/<slug:cat>/', views.categories),
]