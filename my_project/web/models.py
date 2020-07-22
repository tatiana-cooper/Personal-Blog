from django.db import models
from datetime import datetime


class Publication(models.Model):
    """ Class represents the sqlite3 database """

    # the title of publication
    title = models.CharField(max_length=128)
    # the text of publication
    text = models.TextField()
    # the date of publication
    date = models.DateTimeField(default=datetime.now)
