from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from sets import views

# Create a router and register the viewset
router = DefaultRouter()
router.register(r'students', views.StudentViewSet, basename='student')

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include(router.urls)),
    path('api-auth/', include('rest_framework.urls')),
]
