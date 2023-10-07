from django.urls import include, path
from rest_framework.routers import DefaultRouter
from rest_framework.authtoken.views import obtain_auth_token

from . import views

router = DefaultRouter()
router.register("menu", views.MenuViewSet, basename="menu")
router.register("booking", views.BookingViewSet, basename="booking")

urlpatterns = [
    path("", include(router.urls)),
    path("api-token-auth/", obtain_auth_token),
]
