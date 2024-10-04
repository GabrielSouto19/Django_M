
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from cars.views import show_cars,new_car
from accounts.views import register_user,login_view,logout_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',view=register_user,name="register_user"),
    path('login/',view=login_view,name="login"),
    path('logout/',view=logout_view,name="logout"),
    path('cars/',view=show_cars,name="cars_list"),
    path('new_car/',view=new_car,name="new_car"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
