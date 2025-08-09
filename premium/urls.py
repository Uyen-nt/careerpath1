from django.urls import path
from . import views


app_name = 'premium'

urlpatterns = [
    path('', views.premium_home, name='premium_home'),
    path('start-trial/', views.start_trial, name='start_trial'),
    path('renew/', views.renew_premium, name='renew_premium'),
    path('initiate-payment/', views.initiate_payment, name='initiate_payment'),
    path('confirm-payment/<int:transaction_id>/', views.confirm_payment, name='confirm_payment'),
    path('payment-success/<int:user_id>/<int:months>/', views.payment_success, name='payment_success'),
]
