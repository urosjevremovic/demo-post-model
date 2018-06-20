from django.db import models
from django.db.models.signals import pre_save
from django.utils import timezone
from django.utils.text import slugify

from .validators import validate_users_mail

PUBLISH_CHOICES = (
    ('draft', 'Draft'),
    ('publish', 'Publish'),
    ('private', 'Private'),
)


class PostManager(models.Manager):
    def all(self, *args, **kwargs):
        qs = super().filter(active=True)
        return qs


class Post(models.Model):
    id = models.BigAutoField(primary_key=True)
    active = models.BooleanField(default=True)
    title = models.CharField(max_length=255, verbose_name='Post title', unique=True)
    slug = models.SlugField(null=True, blank=True)
    content = models.TextField(null=True, blank=True)
    publish = models.CharField(max_length=120, choices=PUBLISH_CHOICES, default='draft')
    view_count = models.PositiveIntegerField(default=0)
    publish_date = models.DateTimeField(auto_now=False, auto_now_add=False, default=timezone.now)
    users_email = models.CharField(max_length=100, validators=[validate_users_mail, ], null=True, blank=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    objects = models.Manager()
    active_posts = PostManager()

    class Meta:
        verbose_name = 'Post'
        verbose_name_plural = 'Posts'

    def __str__(self):
        return self.title


def post_model_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.title)


pre_save.connect(post_model_pre_save_receiver, sender=Post)
