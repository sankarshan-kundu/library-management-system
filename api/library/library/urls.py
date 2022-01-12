from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path('lms/', include('lms.urls')),
    path('admin/', admin.site.urls),
]