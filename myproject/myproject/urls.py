# myproject/urls.py

from django.urls import include, path
from rest_framework.routers import DefaultRouter
from myapp.views import UserViewSet

router = DefaultRouter()
router.register(r'users', UserViewSet)

urlpatterns = [
    path('api/', include(router.urls)),
]
