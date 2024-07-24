from django.db import models

# Create your models here.
from django.db import models

class Password(models.Model):
    length = models.IntegerField()
    include_uppercase = models.BooleanField(default=True)
    include_lowercase = models.BooleanField(default=True)
    include_numbers = models.BooleanField(default=True)
    include_special = models.BooleanField(default=True)
    generated_password = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
