from django.contrib import admin

from .models import Post


class PostAdmin(admin.ModelAdmin):
    fields = (
        'title',
        'slug',
        'content',
        'publish',
        'publish_date',
        'active',
        'timestamp',
        'updated',
    )
    readonly_fields = (
        'timestamp',
        'updated',
    )

    class Meta:
        model = Post


admin.site.register(Post, PostAdmin)
