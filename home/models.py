from django.db import models


class ContactMessage(models.Model):
    name = models.CharField(max_length=32)
    email = models.EmailField()
    message = models.TextField()

    def __str__(self):
        return self.name + ', ' + self.message[:10]
