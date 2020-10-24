from django.contrib.auth.mixins import LoginRequiredMixin, PermissionRequiredMixin, UserPassesTestMixin
from django.shortcuts import render, get_object_or_404, redirect
from django.urls import reverse, reverse_lazy
from django.views.generic import ListView, DetailView, CreateView, UpdateView, DeleteView
from django.views.generic.base import View

from accounts.models import Profile
from webapp.forms import PhotoForm, FavoriteAddForm
from webapp.models import Photo, Favorite


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

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        return context




class PhotoCreate(LoginRequiredMixin, CreateView):
    template_name = 'photo/create.html'
    form_class = PhotoForm
    model = Photo

    #def form_valid(self, form):
    #    form.instance.author = self.request.user
    #    return super().form_valid(form)

    def get_success_url(self):
        return reverse('webapp:photo_detail', kwargs={'pk': self.object.pk})


class PhotoUpdateView(PermissionRequiredMixin, UpdateView):
    model = Photo
    template_name = 'photo/update.html'
    form_class = PhotoForm
    permission_required = 'webapp.change_project'

    def has_permission(self):
        article = self.get_object()
        return super().has_permission() or article.author == self.request.user


class Delete_Photo(UserPassesTestMixin, DeleteView):
    template_name = 'photo/del_photo.html'
    model = Photo
    context_key = 'photo'
    success_url = reverse_lazy('webapp:index')

    def test_func(self):
        return self.request.user.has_perm('webapp.del_photo') or \
               self.get_object().author == self.request.user


class FavoriteView(CreateView):
    model = Favorite
    form_class = FavoriteAddForm

    def post(self, request, *args, **kwargs):
        self.photo = get_object_or_404(Photo, pk=self.kwargs.get('pk'))
        return super().post(request, *args, **kwargs)

    def form_valid(self, form):
        try:
            cart_product = Favorite.objects.get(product=self.photo, pk__in=self.get_cart_ids())

            cart_product.save()
        except Favorite.DoesNotExist:
            cart_product = Favorite.objects.create(product=self.photo)
            self.save_to_session(cart_product)

        return redirect(self.get_success_url())

    def form_invalid(self, form):
        return redirect(self.get_success_url())

    def get_success_url(self):
        if next:
            return next
        return reverse('webapp:index')

    def get_cart_ids(self):
        return self.request.session.get('cart_ids', [])

    def save_to_session(self, cart_product):
        cart_ids = self.request.session.get('cart_ids', [])
        if cart_product.pk not in cart_ids:
            cart_ids.append(cart_product.pk)
        self.request.session['cart_ids'] = cart_ids

