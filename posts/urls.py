from django.urls import path
from . views import UserViewSet
from . views import PostViewSet
from rest_framework.routers import SimpleRouter

router = SimpleRouter()

router.register('', UserViewSet, basename='users')
router.register('post', PostViewSet, basename='post')
urlpatterns = router.urls