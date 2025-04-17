from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name=models.CharField(max_length=150,null=False,blank=False,unique=True,verbose_name="Kategoriya nomi")
    created_at=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)

    class Meta:
        verbose_name="Kategoriya"
        verbose_name_plural="Kategoriyalar"

    def __str__(self):
        return self.name

class New(models.Model):

    class Status(models.TextChoices):
        Draft="DF","Draft"
        Published="PB","Published"

    title=models.CharField(max_length=200,null=False,blank=False,verbose_name="Yangilik sarlavhasi")
    category=models.ForeignKey(Category,on_delete=models.CASCADE)
    slug=models.SlugField(max_length=200)
    body=models.TextField()
    image=models.ImageField(upload_to="news/",null=True,blank=True)
    created_at=models.DateTimeField(auto_now_add=True)
    published_at=models.DateTimeField(auto_now=True)
    updated_at=models.DateTimeField(auto_now=True)
    status=models.CharField(max_length=2,choices=Status.choices,default=Status.Draft)

    def __str__(self):
        return self.title

    class Meta:
        ordering=["-published_at"]
        verbose_name="Yangilik"
        verbose_name_plural="Yangiliklar"



class Comment(models.Model):
    user=models.ForeignKey(User,on_delete=models.CASCADE)
    new=models.ForeignKey(New,on_delete=models.CASCADE)
    comment=models.TextField()
    created=models.DateTimeField(auto_now_add=True)
    updated_at=models.DateTimeField(auto_now=True)
    status=models.BooleanField(default=True)

    def __str__(self):
        return f"{self.user} - {self.new} - {self.comment}"

    class Meta:
        ordering=["-created"]








