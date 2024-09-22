from django.contrib import admin
from django.urls import path, include
from .views import home  # Add this line

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/", include('account.urls')),
    path('', home, name='home'),  # Add this line
]
