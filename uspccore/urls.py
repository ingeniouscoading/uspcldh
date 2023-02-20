<<<<<<< Updated upstream
"""uspccore URL Configuration
=======
>>>>>>> Stashed changes
"""
uspccore URL Configuration
"""

from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('', include('uspcldh.urls')),
    path('admin/', admin.site.urls),
]


# Admin Pannel Changes 
admin.site.site_header = "USPC Administrator"
admin.site.site_title = "USPC Admin Portal"
admin.site.index_title = "Welcome to USPC Admin Portal"