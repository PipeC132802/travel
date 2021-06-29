from django.contrib import admin
from django.urls import include, path

admin.autodiscover()

urlpatterns = [
    path('places/', include('api.places.urls')),
]