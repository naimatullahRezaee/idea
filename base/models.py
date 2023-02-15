from django.db import models
from django.contrib.auth.models import User
# Create your models here.


class Company(models.Model):
    name = models.CharField(max_length=200)
    bio = models.TextField(null=True, blank=True)
    #tags
    website = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self):
        return self.name
    

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE, null=True, blank=True)
    # image = models.ImageField()
    name = models.CharField(max_length=200)
    social = models.ManyToManyField('Social', null=True, blank=True)
    skill = models.ManyToManyField('Skill',  null=True, blank=True)

    def __str__(self): 
        return self.name

class Review(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField()
    created = models.DateTimeField(auto_now_add=True)


    def __str__(self): 
        return self.body

class Social(models.Model):
    icon  = models.ImageField(default='', upload_to="", blank=True, null=True)
    link = models.CharField(max_length=500, null=True, blank=True)

    def __str__(self): 
        return self.link

class Skill(models.Model):
    name  = models.CharField(max_length=200, null=True, blank=True)

    def __str__(self): 
        return self.name


class Post(models.Model):
    POST_TYPE =( 
        ('collab', 'collab'),
        ('job', 'job'),
        ('default', 'default'), 
    )
    woner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post_ty =models.CharField(max_length=200 ,choices=POST_TYPE, default=POST_TYPE[2])
    body = models.TextField(null=True, blank=True)
    likes = models.ManyToManyField(User, related_name="likes", null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:30]

class Like(models.Model):
    owner= models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)

class Comment(models.Model):
    owner = models.ForeignKey(User, on_delete=models.CASCADE, null=True, blank=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, null=True, blank=True)
    body = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.body[0:30]    