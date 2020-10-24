from django.shortcuts import render
from django.urls import reverse
from django.views.generic import ListView, DetailView, CreateView

from webapp.forms import PhotoForm
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




class PhotoCreate(CreateView):
    template_name = 'photo/create.html'
    form_class = PhotoForm
    model = Photo

    #def form_valid(self, form):
    #    form.instance.author = self.request.user
    #    return super().form_valid(form)

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})
