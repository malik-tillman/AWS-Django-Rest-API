from django.contrib import admin
from django.conf.urls import url
from django.urls import path, include
from projects.views import ProjectView
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'projects', ProjectView)

urlpatterns = [
    path('', include(router.urls)),
    path("projects/", ProjectView),
    path("admin/", admin.site.urls),
    path("api-auth/", include('rest_framework.urls'))
]
