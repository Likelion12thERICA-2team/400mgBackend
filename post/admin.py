from django.contrib import admin
from .models import Post, Reply, Scrap

# Register your models here.

admin.site.register(Post)
admin.site.register(Reply)
admin.site.register(Scrap)
