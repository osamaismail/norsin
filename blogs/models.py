from django.db import models
from norsin.utils import unique_slug_generator
# from autoslug import AutoSlugField
from django.db.models.signals import pre_save
from accounts.models import Blogger
from PIL import Image
from django.urls import reverse
from tinymce import HTMLField

class Category(models.Model):
    title = models.CharField(blank=True, max_length=100)

    class Meta:
        verbose_name_plural = "Categories"

    def __str__(self):
        return self.title

# class PostView(models.Model):
#     user = models.ForeignKey(User, on_delete=models.CASCADE)
#     post = models.ForeignKey('Post', on_delete=models.CASCADE)


class Post(models.Model):
    title = models.CharField(blank=True, max_length=100, verbose_name='عنوان المقال')
    slug = models.SlugField(blank=True, unique=True, allow_unicode=True)
    overview = models.TextField(blank=True, verbose_name='المقدمة')
    content = HTMLField(verbose_name='المقال')
    timestamp = models.DateTimeField(auto_now_add=True)
    comment_count = models.IntegerField(default=0)
    view_count = models.IntegerField(default=0)
    author = models.ForeignKey(Blogger, on_delete=models.CASCADE)
    thumbnail = models.ImageField(upload_to="post_thumbnail/", verbose_name='صورة المقال')
    categories = models.ManyToManyField(Category, verbose_name='التصنيفات')
    featured = models.BooleanField(default=False, verbose_name='المميز')
    deleted = models.BooleanField(default=False)
    # pre_post = models.ForeignKey('self', related_name='previous_post' ,on_delete=models.SET_NULL, blank=True, null=True)
    # nex_post = models.ForeignKey('self', related_name='next_post' ,on_delete=models.SET_NULL, blank=True, null=True)


    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super(Post, self).save(*args, **kwargs)
        thumbnail = Image.open(self.thumbnail.path)
        if thumbnail.height > 400 or thumbnail.width > 400:
            output_size = (400, 400)
            thumbnail.thumbnail(output_size)
            thumbnail.save(self.thumbnail.path)

    def get_absolute_url(self):
        return reverse('post_detial', kwargs={'slug':self.slug})

    def get_update_url(self):
        return reverse('post_detial', kwargs={'slug':self.slug})

    def get_delete_url(self):
        return reverse('post_detial', kwargs={'slug':self.slug})

def post_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)

pre_save.connect(post_pre_save_receiver, sender=Post)

# @property
#
# def view_count(self):
#     return PostView.objects.filter(post=self).count()



#     @property
#     def get_comments(self):
#         return self.comments.all().order_by('-timestamp')
#
# class Comment(models.Model):
#     user = models.CharField(blank=True, max_length=100)
#     timestamp = models.DateTimeField(auto_now_add=True)
#     content = models.TextField(blank=True)
#     email = models.EmailField()
#     post = models.ForeignKey(Post, related_name='comments', on_delete=models.CASCADE)
#     accepted = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.email
