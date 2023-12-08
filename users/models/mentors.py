from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Mentor(models.Model):
    user = models.OneToOneField(
            to=User,
            on_delete=models.PROTECT,
            related_name="mentor",
            verbose_name="Ментор"
        )
    name = models.CharField(max_length=60)
    description = models.TextField(null=True,blank=True)

    def __str__(self):
        return self.name