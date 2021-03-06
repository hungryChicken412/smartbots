"""SMS URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static  import static
from .views import home_view, register, logout_request, login_request, landing, dashboard, cost

from profiles.models import Profile
from profiles.views import ProfileViewSet, ChatbotTalkViewSet
from rest_framework import routers, serializers, viewsets
from django.contrib.auth import views as auth_views
from rest_framework.authtoken.views import ObtainAuthToken
from django.views.decorators.csrf import csrf_exempt




# Routers provide an easy way of automatically determining the URL conf.
router = routers.DefaultRouter()
router.register(r'(?P<token>[-\w]+)', ChatbotTalkViewSet, basename='talkView')


# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.



app_name = "app"
urlpatterns = [
    path('api/', include(router.urls)),
    path('auth/', csrf_exempt(ObtainAuthToken.as_view())), #path('auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('admin/', admin.site.urls),

    path('', landing, name="landing"),
    path('costRegistration/', cost),
    
    path('tinymce/', include('tinymce.urls')),
    path('app/', dashboard, name="app-dashboard"),
    path('register/', register, name="register"),
    path('logout/', logout_request, name="logout"),
    path('login/', login_request, name="login"),



    
      # Password reset links (ref: https://github.com/django/django/blob/master/django/contrib/auth/views.py)
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(template_name='password_reset/password_change_done.html'), 
        name='password_change_done'),

    path('password_change/', auth_views.PasswordChangeView.as_view(template_name='password_reset/password_change.html'), 
        name='password_change'),

    path('password_reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_done.html'),
     name='password_reset_done'),

    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="password_reset/password_reset_confirm.html"), name='password_reset_confirm'),
    path('password_reset/', auth_views.PasswordResetView.as_view(template_name='password_reset/password_reset_form.html'), name='password_change'),

    
    
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(template_name='password_reset/password_reset_complete.html'),
     name='password_reset_complete'),



]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)



