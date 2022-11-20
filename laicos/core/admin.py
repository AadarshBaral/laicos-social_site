from django.contrib import admin
from .models import Profile, Post,LikePost,FollowersCount
# Register your models here.

admin.site.register(Profile)
admin.site.register(Post)
admin.site.register(LikePost)
admin.site.register(FollowersCount)
# @admin.register(Profile)
# class PostAdmin(admin.ModelAdmin):
#     list_display =