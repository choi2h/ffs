from django.contrib import admin
from django.urls import path
from ninja import NinjaAPI

from apps.users.urls import router as user_router

base_api = NinjaAPI(title="FFS", version="0.0.0")
base_api.add_router("users", user_router)

urlpatterns = [
    path("", base_api.urls),
    path('admin/', admin.site.urls),
]
