from django.db import models
from django.utils.translation import gettext_lazy as _
from django.contrib.auth.views import LoginView

from users.models import MyUser


# class Comment(models.Model):
#     pass
#
#
# class Post(models.Model):
#
#     title = models.CharField(_('title'), max_length=60, blank=False)
#     # slug = models.SlugField(_('slug'), max_length=255, unique=True, blank=True)
#     image = models.ImageField(_('image'), default='default.jpg', upload_to='post_pics/%Y/%m/%d/')
#     content = models.TextField(_('content'), blank=False)
#     date_posted = models.DateTimeField(_('date posted'), auto_now_add=True)
#     date_updated = models.DateTimeField(_('date updated'), auto_now=True)
#     is_edited = models.BooleanField(_('edited'), default=False)
#     like = models.IntegerField(_('like'), default=0)
#     dislike = models.IntegerField(_('dislike'), default=0)
#     comment = models.ManyToManyField(Comment, blank=True)
#     author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
#
#     def __str__(self):
#         return self.title
#
#     class Meta:
#         db_table = 'Posts'
#         verbose_name = _('post')
#         verbose_name_plural = _('posts')
