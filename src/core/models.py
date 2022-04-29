from django.db import models
from django.utils import timezone
from datetime import datetime


def upload_to(instance, filename):
    return filename.format(filename=filename)


class Items(models.Model):
    image = models.CharField(max_length=200)
    title = models.CharField(max_length=100)
    cost = models.CharField(max_length=25)
    description = models.TextField(max_length=350)
    description_large = models.TextField(max_length=500)


class Details(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    company = models.CharField(max_length=200)
    choice = models.CharField(max_length=200)


class Customer(models.Model):
    name = models.CharField(max_length=200)
    city = models.CharField(max_length=200)
    email = models.CharField(max_length=200)
    phone = models.CharField(max_length=30)
    company = models.CharField(max_length=200)
    choice = models.CharField(max_length=200)
    themessage = models.TextField(max_length=100)

    def __str__(self):
        return self.name


class SiteImages(models.Model):
    alt_text = models.CharField(max_length=250)
    image = models.ImageField(upload_to=upload_to)

    def __str__(self):
        return self.alt_text


class Articles(models.Model):
    title = models.CharField(max_length=250)
    excerpt = models.TextField()
    content1 = models.TextField(blank=True)
    content2 = models.TextField(blank=True)
    content3 = models.TextField(blank=True)
    content4 = models.TextField(blank=True)
    subContent1 = models.TextField(blank=True)
    subContent2 = models.TextField(blank=True)
    image1 = models.ImageField(upload_to=upload_to)
    image2 = models.ImageField(upload_to=upload_to)
    published = models.DateTimeField(default=timezone.now)
    publishedDay = models.DateField(default=datetime.today().weekday())
    isFeatured = models.BooleanField(default=False)

    class Meta:
        ordering = ('-published',)

    def __str__(self):
        return self.title


class AgricultureSignUp(models.Model):
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    isFree = models.BooleanField(default=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class RetailSignUp(models.Model):
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    isFree = models.BooleanField(default=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class EducationSignUp(models.Model):
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)
    isFree = models.BooleanField(default=True)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class ContactEmail(models.Model):
    fullName = models.CharField(max_length=250, blank=True, null=True)
    companyName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    phoneNumber = models.CharField(max_length=250, blank=True, null=True)
    message = models.TextField(blank=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class EnquiryEmail(models.Model):
    fullName = models.CharField(max_length=250, blank=True, null=True)
    email = models.EmailField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.fullName


class Newsletter(models.Model):
    email = models.EmailField(blank=True, null=True)
    timestamp = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-timestamp',)

    def __str__(self):
        return self.email
