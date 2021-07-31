from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDB(models.Model):
    #user = models.ForeignKey(User, on_delete=models.CASCADE)
    user = models.CharField(max_length=200, default='', null=False)
    title = models.CharField(max_length=500, default='', null=False)
    content = models.TextField()
    author = models.ForeignKey(User, default=None, on_delete=models.CASCADE)


    def __str__(self):
        return self.title
