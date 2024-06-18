
from django.urls import path
from client import views

urlpatterns = [
    path('',views.index),
    path('client_RL/', views.client_RL),
    path('client_login/',views.client_login),
    path('client_logout/',views.client_logout),
    path('client_home/',views.client_home),
    path('client_req/',views.client_req),
    path('client_checkpoints/', views.client_checkpoints),
    path('payment/',views.payment),
    path('process_payment/',views.process_payment),


]
