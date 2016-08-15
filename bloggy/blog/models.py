from django.db import models
class Category(models.Model):
    name = models.CharField(max_length = 255)

    def __unicode__(self):
        return self.name

    def __str__(self):
        return self.name

class User(models.Model):
    username = models.CharField(verbose_name=("Username"), max_length = 16)
    password = models.CharField(verbose_name=("Password"),max_length = 16)
    email = models.EmailField(verbose_name=("Email Adress"))
    level = models.IntegerField(editable=False,default=1)
    authority = models.IntegerField(editable=False, default=1)

    def __str__(self):
        return self.username


class Post(models.Model):
    title = models.CharField(max_length = 255)
    category = models.ManyToManyField('Category')
    description = models.TextField(blank=True, null = True)
    body = models.TextField()
    author = models.ForeignKey('User')
    creationDate = models.DateTimeField()
    isPublished = models.BooleanField(default=False)

    def __unicode__(self):
        return self.title

    def __str__(self):
        return str(self.title) + "Category : " + str(self.category)


class Comment(models.Model):
    body = models.TextField()
    name = models.CharField(max_length= 255)
    date_creation = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post)

    def __str__(self):
        return self.body
