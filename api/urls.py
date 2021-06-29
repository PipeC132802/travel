from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path('auth/', include('api.app_auth.urls')),
    path('places/', include('api.places.urls')),
]
