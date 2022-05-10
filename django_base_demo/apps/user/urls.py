from rest_framework import routers

from . import views

urlpatterns = []
router = routers.DefaultRouter()

router.register(r'', views.UserViewSet, basename='user')

urlpatterns += router.urls
