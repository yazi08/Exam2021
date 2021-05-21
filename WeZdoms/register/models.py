from django.db import models
from django.urls import reverse
# Create your models here.

class Mudrosty (models.Model):
    data_blog = models.DateTimeField('Дата публикации',auto_now_add =True, null=True)
    description_blog = models.TextField('Фраза', null=True)
    name_blogers = models.TextField('Имя блогера')



    def __str__(self):
        return f"{self.description_blog}"


