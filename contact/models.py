from django.db import models

""" Create your models here.

 Model to store contact form submissions,
 including name, email, message, and read status"""


class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    is_read = models.BooleanField(default=False)  # To mark requests as "read"
    submitted_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"
