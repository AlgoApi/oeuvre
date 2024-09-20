from django.contrib import admin
from .models import TgUser, AgentId

# Register your models here.

admin.site.register(TgUser)
admin.site.register(AgentId)
