from django.contrib import admin

from models import UserProfile,Post,Message,ProfileFeedback,PostFeedback

admin.site.register(UserProfile)
admin.site.register(Post)
admin.site.register(PostFeedback)
admin.site.register(ProfileFeedback)
admin.site.register(Message)


# Register your models here.
