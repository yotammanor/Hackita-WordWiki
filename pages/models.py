from django.db import models
from django.core.validators import RegexValidator
# Create your models here.


class Page(models.Model):
    word = models.CharField(max_length=32,
                            primary_key=True,
                            db_index=True,
                            validators=[RegexValidator(regex=r'[a-z]*')])
    content = models.TextField()
    creation_date = models.DateField()
    #creator = models.CharField(max_length=32)
