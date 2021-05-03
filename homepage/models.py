from django.db import models

# Create your models here.


class Admin(models.Model):
    id = models.AutoField(db_column='id', primary_key=True)
    heading = models.CharField(max_length=500, null=True)
    heading_url = models.TextField(null=True)
    view = models.CharField(max_length=250, null=True)
    is_filled = models.IntegerField(default=0)
    is_empty = models.IntegerField(default=0)

    def __str__(self):
        return self.heading

    class Meta:
        db_table = 'homepage_info'
