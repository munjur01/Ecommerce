from django.db import models

# Create your models here.
class ContactInfo(models.Model):
    name = models.CharField(max_length=50)
    email = models.EmailField()
    phone = models.CharField(max_length=13)
    subject = models.CharField(max_length=200)
    message = models.TextField()

    class Meta:
        verbose_name_plural = 'Contact Info'

    def __str__(self):
        return self.email