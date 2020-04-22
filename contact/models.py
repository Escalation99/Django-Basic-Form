from django.db import models

# Create your models here.


class PostModel(models.Model):
    nama = models.CharField(max_length=20)
    gender = models.CharField(max_length=20)
    email = models.EmailField()
    alamat = models.CharField(max_length=200)
    #agree = models.BooleanField()
    published = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return "{}. {}".format(self.id, self.nama)
