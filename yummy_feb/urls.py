"""
URL configuration for yummy_feb project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from main import views as main_views
from manager import views as manager_views
from django.conf.urls.static import static
from yummy_feb import settings
from account import views as account_views
from django.contrib.auth import views as auth_views
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', main_views.index, name='home'),
    path('manager/', manager_views.index, name='manager'),

    path(settings.LOGIN_URL, account_views.UserLoginView.as_view(), name='login'),
    path('account/register/', account_views.UserRegistrationView.as_view(), name='register'),
    path('account/logout/', account_views.user_logout, name='logout'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
