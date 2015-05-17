from django.conf import settings
from django.db import models

from hashids import Hashids


class Paste(models.Model):
    unique_id = models.CharField(max_length=50, null=True)
    title = models.CharField(max_length=500)
    content = models.TextField(blank=False)

    def __str__(self):
        return self.title

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.unique_id:
            hashids = Hashids(salt=settings.SECRET_KEY, min_length=8)
            self.unique_id = hashids.encode(self.id)
            super().save(*args, **kwargs)
