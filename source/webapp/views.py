from django.shortcuts import render
from django.views.generic import ListView, DetailView

from webapp.models import Photo


class PhotoListView(ListView):
    template_name = 'photo/index.html'
    context_object_name = 'photos'
    model = Photo
    #paginate_by = 10
    #paginate_orphans = 0

    def get(self, request, *args, **kwargs):
        return super().get(request, *args, **kwargs)

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(object_list=object_list, **kwargs)
        return context



class PhotoDetail(DetailView):
    template_name = 'photo/photo_detail.html'
    model = Photo
