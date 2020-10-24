from django.shortcuts import render
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView

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
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class PhotoUpdateView(UpdateView):
    model = Photo
    template_name = 'photo/update.html'
    form_class = PhotoForm
    #permission_required = 'webapp.change_project'


    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        #context['users'] = User
        return context

    def get_success_url(self):
        return reverse('photo_detail', kwargs={'pk': self.object.pk})


class Delete_Photo(DeleteView):
    template_name = 'photo/del_photo.html'
    model = Photo
    context_key = 'photo'
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        return self.request.user.has_perm('webapp.del_photo') or \
               self.get_object().author == self.request.user
