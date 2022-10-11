from distutils.command.upload import upload
from email.mime import image
from django.db import models
from django.contrib.auth.models import User
from django.urls import reverse
from ckeditor.fields import RichTextField


class BlogPost(models.Model):
    Author = models.ForeignKey(User, on_delete=models.CASCADE,)
    Title = models.CharField(max_length=255)
    Images =models.ImageField(blank=True,null=True, upload_to="images/user_upload")
    Date_Created=models.DateTimeField(auto_now=True)
    Body= RichTextField(blank=True, null=True)
    def __str__(self):
        return (self.Title+" " +"|By:"+" " +str(self.Author))
    
    def get_absolute_url(self):
        return reverse('main:home', args=(str(self.pk)))

class Profile(models.Model):
    user=models.OneToOneField(User, related_name='picture',
                              on_delete=models.CASCADE)
    Profile_pic =models.ImageField(blank=True,null=True, upload_to="images/profile_pic")
    def __str__(self):
        return str(self.user)

class Comment_post(models.Model):
    post = models.ForeignKey(User, related_name ='comment',on_delete=models.CASCADE,)
    name=models.CharField(max_length=255)
    body=  models.TextField()
    date_added= models.DateTimeField(auto_now_add=True)
    
    def __str__(self):
        return '%s - %s' %(self.post.Title, self.name)