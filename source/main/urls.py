"""main URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.conf.urls.static import static
from django.conf import settings
from django.contrib import admin
from django.urls import path, include

from webapp.views import PhotoListView, PhotoDetail, PhotoCreate, PhotoUpdateView,\
Delete_Photo

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('', include('webapp.urls')),
    path('api-auth/', include('rest_framework.urls', namespace='rest_framework')),
    path('api/', include('api.urls')),

    path('', PhotoListView.as_view(), name='index'),
    path('photo/<int:pk>/', PhotoDetail.as_view(), name='photo_detail'),
    path('photo/<int:pk>/update', PhotoUpdateView.as_view(), name='photo_update'),
    path('photo/<int:pk>/del/', Delete_Photo.as_view(), name='del'),
    path('photo/create/', PhotoCreate.as_view(), name='photo_create'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
