from django.contrib import admin
from django.urls import path
from django.conf.urls import include
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('techpit/admin/', admin.site.urls),
    path('techpit/amazon/', include('amazon.urls'))
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
