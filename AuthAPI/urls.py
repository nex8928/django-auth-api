from django.contrib import admin
from django.urls import path, include
from .views import home, login_view, dashboard_view, logout_view  # Add these imports

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/user/", include('account.urls')),
    path('', home, name='home'),
    path('login/', login_view, name='login'),  # Add this line
    path('dashboard/', dashboard_view, name='dashboard'),  # Add this line
    path('logout/', logout_view, name='logout'),  # Add this line
]
