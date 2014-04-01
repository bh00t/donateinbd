from django.contrib import admin

from models import UserProfile,Post,Message,ProfileFeedback,PostFeedback,Report

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(PostFeedback)
admin.site.register(ProfileFeedback)
admin.site.register(Message)
admin.site.register(Report)


# Register your models here.
