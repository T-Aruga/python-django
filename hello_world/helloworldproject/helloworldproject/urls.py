from django.contrib import admin
from django.urls import path, include
from .views import HelloWorldView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('hello/', include('helloworldapp.urls')),
]
