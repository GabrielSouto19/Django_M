
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from cars.views import CarsView,NewCarView
from accounts.views import register_user,login_view,logout_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',view=register_user,name="register_user"),
    path('login/',view=login_view,name="login"),
    path('logout/',view=logout_view,name="logout"),
    path('cars/',view=CarsView.as_view(),name="cars_list"),
    path('new_car/',view=NewCarView.as_view(),name="new_car"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
