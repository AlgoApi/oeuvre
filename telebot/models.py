from django.db import models


class TgUser(models.Model):
    tg_url = models.URLField()
    tg_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    description = models.TextField()


class AgentId(models.Model):
    id = models.IntegerField()

    def __str__(self):
        return self.id
