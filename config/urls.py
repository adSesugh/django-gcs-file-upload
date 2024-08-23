from django.contrib import admin
from django.urls import path
from core.views import RegisterUserAPIView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/', RegisterUserAPIView.as_view(), name='register'),
]
