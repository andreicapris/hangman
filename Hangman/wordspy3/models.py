from django.db import models
from django.utils import timezone


class AddWord(models.Model):
    cat = models.ForeignKey('auth.User')
    definition = models.TextField(max_length=34)
    length = models.TextField(max_length=2)
    addate = models.DateTimeField(default=timezone.now)

    @property
    def __push__(self):
        if (self.length != 0):
            return self.definition

    def added_date(self):
        self.addate = timezone.now()
        self.save()
