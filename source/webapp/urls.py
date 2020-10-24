from django.urls import path, include
from webapp.views import PhotoListView, PhotoDetail, PhotoCreate, PhotoUpdateView,\
Delete_Photo, FavoriteView

app_name = 'webapp'

urlpatterns = [
    path('', PhotoListView.as_view(), name='index'),
    path('<int:pk>/', PhotoDetail.as_view(), name='photo_detail'),
    path('<int:pk>/update', PhotoUpdateView.as_view(), name='photo_update'),
    path('<int:pk>/del/', Delete_Photo.as_view(), name='del'),
    path('create/', PhotoCreate.as_view(), name='photo_create'),

    path('<int:pk>/add/', FavoriteView.as_view(), name='favorite'),
]