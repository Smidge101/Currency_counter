
from django.contrib import admin
from django.urls import path, include  # Don't forget to include

urlpatterns = [
    path('admin/', admin.site.urls),  # Admin panel URL
    path('currency/', include('myapp.urls')),  # Include the URLs from the 'currency' app
]