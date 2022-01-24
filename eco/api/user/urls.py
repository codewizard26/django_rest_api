from django.contrib.auth import logout
from rest_framework import routers
from django.urls import path,include

from . import views


router = routers.DefaultRouter()
router.register(r'',views.UserViewSet)

urlpatterns = [
    path('login/',views.signin,name='signin'),
    path('logout/<int:id>/',views.logout,name = 'logout'),
    path('',include(router.urls))
]