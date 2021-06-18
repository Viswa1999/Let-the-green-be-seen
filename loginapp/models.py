from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    fname = models.CharField(max_length=30)
    lname = models.CharField(max_length=30)
    email = models.CharField(max_length=30)
    password = models.CharField(max_length=30)
    repassword = models.CharField(max_length=30)

"""class Image(models.Model):
    caption = models.CharField(max_length=100)
    image = models.ImageField(upload_to="img/%y")
    def __str__(self):
        return self.caption"""