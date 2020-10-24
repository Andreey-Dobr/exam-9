from django.contrib.auth import get_user_model
from django.db import models



class Photo(models.Model):
    photo = models.ImageField(null=False,  upload_to='user_pics', verbose_name='Аватар')
    label = models.TextField(max_length=3000, null=False, verbose_name='подпись')
    created_at = models.DateTimeField(auto_now_add=True, verbose_name='Время создания')
    author = models.ForeignKey(get_user_model(), null=False, on_delete=models.SET_DEFAULT, default=1,
                               related_name='photos', verbose_name='Автор')

    def __str__(self):
        return "{}. {}".format(self.pk, self.label)

    class Meta:
        verbose_name = 'Фото'
        verbose_name_plural = 'Фотографии'


class Favorite(models.Model):
    photo = models.ForeignKey('webapp.Photo', on_delete=models.CASCADE,
                                verbose_name='избраное', related_name='in_favorite')


