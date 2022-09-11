
from django.urls import path, include
from .views import  UserViewSet,CustomAuthToken

from rest_framework.routers import DefaultRouter
router = DefaultRouter()
router.register(r'users', UserViewSet, basename='user')
urlpatterns = router.urls

urlpatterns += [
    path('api-token-auth/', CustomAuthToken.as_view())
    
]