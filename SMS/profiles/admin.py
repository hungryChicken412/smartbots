from django.contrib import admin
from .models import Profile, chatlog, faq, ChatbotProfile
# Register your models here.

admin.site.register(Profile)
admin.site.register(faq)
admin.site.register(ChatbotProfile)
admin.site.register(chatlog)
