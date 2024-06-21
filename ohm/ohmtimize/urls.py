from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('clients/', views.ClientsListView.as_view(), name='clients'),
    path('clients/<int:pk>/', views.ClientDetailView.as_view(), name='client-detail'),
    path('installations/', views.InstallationListView.as_view(), name='installations'),
    path('installations/<int:pk>/', views.InstallationDetailView.as_view(), name='installation-detail'),
    path('myconsumption/', views.ConsumptionByUserListView.as_view(), name='myconsumption'),
    path('mydevices/', views.DevicesByUserListView.as_view(), name='mydevices'),
    #path('mydevices/<int:pk>/', views.DeviceDetailView.as_view(), name='device-detail'),
]