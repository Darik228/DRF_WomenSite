from django.urls import path, include, re_path
from .views import *
from rest_framework import routers
from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenObtainPairView

router = routers.DefaultRouter()
router.register(r'women', WomenViewSet)  # basename='best'
print(router.urls)


urlpatterns = [
    path('api/v1/', include(router.urls)),
    # path('api/v1/womenlist/', WomenViewSet.as_view({'get': 'list', 'post': 'create'}), name='home'),
    # path('api/v1/womenlist/<int:pk>/', WomenViewSet.as_view({'put': 'update', 'delete': 'destroy', 'patch': 'retrieve'}), name='update'),
    path('api/v1/womenlist/', WomenApiView.as_view(), name='home'),
    path('api/v1/womenupdate/<int:pk>/', WomenApiUpdateView.as_view()),
    path('api/v1/womendelete/<int:pk>/', WomenApiDeleteView.as_view()),
    path('api/v1/drf-auth/', include('rest_framework.urls')),  # Авторизация на основе сессии и кук
    path('api/v1/auth/', include('djoser.urls')),  # аутентификация по токенам
    re_path(r'^auth/', include('djoser.urls.authtoken')),  # авторизация по токену
    path('api/v1/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),  # JWT
    path('api/v1/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),  # JWT refresh token to get access
    path('api/v1/token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('hi/', index)
]