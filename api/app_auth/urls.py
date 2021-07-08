from django.urls import path, include
from rest_framework import routers

from .views import *

api = routers.SimpleRouter()

urlpatterns = [
    path('', include('dj_rest_auth.urls')),
    path('registration/', include('rest_auth.registration.urls')),
    path('', include(api.urls))
]

"""path('user-auth/facebook/', FacebookLogin.as_view(), name='fb_login'),
    path('user-auth/google/', GoogleLogin.as_view(), name='google_login'),
    path('user-auth/twitter/', TwitterLogin.as_view(), name='twitter_login'),"""