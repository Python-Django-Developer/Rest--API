from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='apiOverview'),

    path('list/', views.ShowAll, name='product-list'),
    path('detail/<int:pk>/', views.ViewProduct, name='product-detail'),
    path('create/', views.CreateProduct, name='product-create'),
    path('update/<int:pk>/', views.updateProduct, name='product-update'),
    path('delete/<int:pk>/', views.deleteProduct, name='product-delete'),


]
