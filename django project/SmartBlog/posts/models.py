from unicodedata import name
from django.db import models
from django.forms import DateTimeField
from django.utils.text import Truncator,slugify
from django.contrib.auth.models import User

# title: character field
# body: text field
# image: character field
# username: character field
# created_at: date time field
# updated_at: date time field
    
    # START CODE HERE

class Post(models.Model):
    title = models.TextField()
    body = models.CharField(max_length=50)
    image = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at =  models.DateTimeField(auto_now=True)
    slug = models.SlugField(default=" ")
    user = models.ForeignKey(User, on_delete=models.CASCADE,null=True,related_name='posts')
    tags = models.ManyToManyField('posts.Tag',related_name='posts')
    
    def save(self, *args, **kwargs):
        self.slug=slugify(self.title)
        super().save()

class Tag(models.Model):
    name=models.CharField(max_length=50)

class User(models.Model):
    username = models.CharField(max_length=60)

    # END CODE