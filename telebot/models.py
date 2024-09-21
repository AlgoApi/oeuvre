from django.db import models


class TgUser(models.Model):
    tg_url = models.URLField()
    tg_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    description = models.TextField()


class AgentId(models.Model):
    id = models.CharField(max_length=30)

    def __int__(self):
        return self.id
