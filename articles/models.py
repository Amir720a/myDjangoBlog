from django.db import models
from django.contrib.auth.models import User

class Articles(models.Model):
    title = models.CharField(max_length=100)
    slug = models.SlugField()
    body = models.TextField()
    date = models.DateField(auto_now_add = True)
    image = models.ImageField(default='default.jpg' , blank=True)
    author = models.ForeignKey(User,default=None,on_delete=models.CASCADE)

    def __str__(self):
        return self.title

    def shortBody(self):
        return self.body[:50] + " ..."

