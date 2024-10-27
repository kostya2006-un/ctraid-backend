from . import views
from rest_framework.routers import SimpleRouter
from django.urls import path, include

router = SimpleRouter()
router.register(r"currency-list", views.CurrencyListView, basename="currency")

app_name = "ctraid"
urlpatterns = [
    path("", include(router.urls)),
]