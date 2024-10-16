from . import views
from rest_framework.routers import SimpleRouter
from django.urls import path, include


router = SimpleRouter()
router.register(r"users", views.UserViewSet, basename="users")
router.register(r"users-list", views.UserList, basename="users-list")


app_name = "users"
urlpatterns = [
    path("", include(router.urls)),
]
