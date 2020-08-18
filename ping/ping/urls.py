from django.contrib import admin
from django.urls import path

from accounts.views import home

from accounts.views import login_view, register_view, logout_view, ip_address
from accounts import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home),
    path('accounts/login/', login_view),
    path('accounts/register/', register_view),
    path('accounts/logout/', logout_view),
#    path('ip_address/', ip_address)
]