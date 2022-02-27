from django.db import models

class Item(models.Model):
    name = models.CharField(max_length=100)
    short_description = models.TextField(max_length=100, blank=True)
    description = models.TextField(blank=True)
    image = models.ImageField(upload_to='media/', blank=True)

    def __str__(self):
        return self.name