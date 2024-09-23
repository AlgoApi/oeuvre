from django.db import models


class TgUser(models.Model):
    tg_url = models.URLField()
    tg_name = models.CharField(max_length=100)
    name = models.CharField(max_length=100)
    photo = models.ImageField(upload_to='images')
    description = models.TextField()
    agent_name = models.CharField(max_length=100)


class AgentId(models.Model):
    id = models.CharField(max_length=30, primary_key=True)

    def __int__(self):
        return self.id
