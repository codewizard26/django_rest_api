from django.contrib import admin
from django.urls import path,include
from django.conf.urls.static import static
from django.conf import settings
from rest_framework import authtoken
from .views import home


urlpatterns = [
    path('',home,name='api.home'),
    path('category/',include('api.category.urls')),
    path('product/',include('api.product.urls')),
    path('user/',include('api.user.urls')),
    path('order/',include('api.order.urls')),
    path('payment/',include('api.payment.urls'))

]