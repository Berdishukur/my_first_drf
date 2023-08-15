from my_api import views
from django.urls import path,include
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'books',views.BookViewSet)
router.register(r'fanlar',views.FanViewSet)
router.register(r'yunalishlar',views.YunalishViewSet)
router.register(r'unversetitlar',views.UnversityViewSet)


urlpatterns = [
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework'))

]


