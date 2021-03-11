from django.contrib import admin
from django.urls import path, include
from core.urls import router
from core.api.viewsets import CustomTokenOptainPairViewSet
from rest_framework_simplejwt.views import TokenRefreshView


urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/", include(router.urls)),
    path(
        'api/token/',
        CustomTokenOptainPairViewSet.as_view(),
        name='token_obtain_pair'
    ),
    path(
        'api/token/refresh/',
        TokenRefreshView.as_view(),
        name='token_refresh'
    ),
]
