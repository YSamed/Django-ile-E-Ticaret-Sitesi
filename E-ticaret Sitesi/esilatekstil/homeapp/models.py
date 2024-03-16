from django.db import models

class Settings(models.Model):
    STATUS = (
        (True, 'Evet'),
        (False, 'Hayır'),
    )
    title = models.CharField(max_length=50)
    keywords = models.CharField(max_length=255)
    descriptions = models.CharField(max_length=255)
    company = models.CharField(max_length=30)
    address = models.CharField(blank=True, max_length=30)
    phone = models.CharField(blank=True, max_length=15)
    fax = models.CharField(blank=True, max_length=30)
    email = models.CharField(blank=True, max_length=30)
    smptserver = models.CharField(blank=True, max_length=20)
    smptemail = models.CharField(blank=True, max_length=50)
    smptpassword = models.CharField(max_length=30)
    smptport = models.CharField(blank=True, max_length=5)
    icon = models.ImageField(blank=True, upload_to='images/')
    instagram = models.CharField(blank=True, max_length=30)
    twitter = models.CharField(blank=True, max_length=30)
    aboutus = models.TextField(blank=True)
    contact = models.TextField(blank=True)
    references = models.CharField(blank=True, max_length=30)
    status = models.BooleanField(choices=STATUS)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
