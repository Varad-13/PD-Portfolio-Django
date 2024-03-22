from django.db import models

from django.db import models

class Project(models.Model):
    name = models.CharField(max_length=255)
    description1 = models.TextField()
    description2 = models.TextField()
    description3 = models.TextField()
    thumbnail = models.ImageField(upload_to='thumbnails/')
    webrender = models.ImageField(upload_to='webrenders/')
    is_top = models.BooleanField(default=False)

class Enquiry(models.Model):
    sender_name = models.CharField(max_length=255)
    sender_email = models.EmailField()
    purpose = models.CharField(max_length=255)
    subject = models.CharField(max_length=255)
    message = models.TextField()

class Socials(models.Model):
    icon = models.ImageField(upload_to='logos/')
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class Skills(models.Model):
    icon = models.ImageField(upload_to='logos/')
    title = models.CharField(max_length=255)
    link = models.CharField(max_length=255)

class Home(models.Model):
    panel_1_image = models.ImageField(upload_to='backgrounds/')
    panel_2_image = models.ImageField(upload_to='thumbnails/')
    panel_3_image = models.ImageField(upload_to='thumbnails/')
    panel_4_image = models.ImageField(upload_to='thumbnails/')
    about_description = models.CharField(max_length=255)