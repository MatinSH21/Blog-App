from django.db import models
from django.utils.translation import gettext_lazy as _
from django.utils.text import slugify

from users.models import MyUser


class Post(models.Model):

    title = models.CharField(_('title'), max_length=60, blank=False)
    slug = models.SlugField(_('slug'), unique=True, blank=True)
    image = models.ImageField(_('image'), default='default.jpg', upload_to='post_pics/%Y/%m/%d/')
    content = models.TextField(_('content'), blank=False)
    date_posted = models.DateTimeField(_('date posted'), auto_now_add=True)
    date_updated = models.DateTimeField(_('date updated'), auto_now=True)
    is_edited = models.BooleanField(_('edited'), default=False)
    like = models.IntegerField(_('like'), default=0)
    dislike = models.IntegerField(_('dislike'), default=0)
    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.title)
        super(Post, self).save(*args, **kwargs)

    class Meta:
        db_table = 'Posts'
        verbose_name = _('post')
        verbose_name_plural = _('posts')


class Comment(models.Model):

    author = models.ForeignKey(MyUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent_comment = models.ForeignKey('self', on_delete=models.SET_NULL, null=True, blank=True, related_name='replies')
    content = models.TextField(_('content'))
    date_created = models.DateTimeField(_('date created'), auto_now_add=True)

    def __str__(self):
        return f'{self.author.username} commented on {self.post.title}'

    class Meta:
        db_table = 'Comments'
        verbose_name = 'comment'
        verbose_name_plural = 'comments'
        ordering = ['-date_created']

    def is_parent_comment(self):
        return self.parent_comment is None

    def get_replies(self):
        return Comment.objects.filter(parent_comment=self)
