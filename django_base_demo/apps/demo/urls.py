from rest_framework import routers

from . import views

urlpatterns = []
router = routers.DefaultRouter()

# router.register(r'', views.DemoViewSet, basename='demo')

urlpatterns += router.urls
