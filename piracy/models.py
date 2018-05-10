from django.db import models


class Pirate(models.Model):
    name = models.CharField(max_length=255)
    is_captain = models.BooleanField()

    class Meta:
        db_table = "pirates"
        app_label = "piracy"
