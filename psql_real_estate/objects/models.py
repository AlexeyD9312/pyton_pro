from django.db import models

class District(models.Model):
    district_ID = models.AutoField(primary_key = True)
    city_ID = models.IntegerField(null = False)
    district_name = models.CharField(max_length = 100)

    def __str__(self):
        return self.name
