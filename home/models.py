from django.db import models

class ECOVolontyor(models.Model):
    fullname = models.CharField(max_length=255)
    university = models.CharField(max_length=255)
    img = models.ImageField(upload_to='media/volontyor')
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.fullname

class NewsCategory(models.Model):
    name = models.CharField(max_length=255)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name

class News(models.Model):
    title = models.CharField(max_length=255)
    img = models.ImageField(upload_to='media/news')
    description = models.TextField()
    post_date = models.DateTimeField(auto_now_add=True)
    see = models.BigIntegerField(default=0)
    category = models.ForeignKey(NewsCategory, on_delete=models.CASCADE, related_name='news')

    def __str__(self):
        return self.title

class Qabul(models.Model):
    url = models.BigIntegerField()

    def __str__(self):
        return self.url

class EDokon(models.Model):
    name = models.CharField(max_length=255)
    price = models.BigIntegerField()
    img = models.ImageField(upload_to='media/edokon')

    def __str__(self):
        return self.name
