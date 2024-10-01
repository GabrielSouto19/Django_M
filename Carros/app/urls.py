
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from django.http import HttpResponse
from cars import views



urlpatterns = [
    path('admin/', admin.site.urls),
    path('cars/',view=views.show_cars),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
