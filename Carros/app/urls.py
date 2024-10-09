
from django.contrib import admin
from django.urls import path,include
from django.conf import settings
from django.conf.urls.static import static
from cars.views import NewCarCreateView,CarsListView,CarDetailView,CarUpdateView
from accounts.views import register_user,login_view,logout_view




urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',view=register_user,name="register_user"),
    path('login/',view=login_view,name="login"),
    path('logout/',view=logout_view,name="logout"),
    path('cars/',view=CarsListView.as_view(),name="cars_list"),
    path('new_car/',view=NewCarCreateView.as_view(),name="new_car"),
    path('car/<int:pk>/',view=CarDetailView.as_view(),name="car_detail"),
    path('car/<int:pk>/update/',view=CarUpdateView.as_view(),name="car_update"),
]+ static(settings.MEDIA_URL,document_root=settings.MEDIA_ROOT)
