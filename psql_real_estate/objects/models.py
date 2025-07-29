from django.db import models
from django.contrib.auth import get_user_model


User = get_user_model()

class District(models.Model):
    district_ID = models.AutoField(primary_key = True)
    city_ID = models.IntegerField(null = False)
    district_name = models.CharField(max_length = 100)
    is_admin_district = models.BooleanField(default = False)
    images = models.ImageField(upload_to = 'district_images/', null = True, blank = True)


    class Meta:
        permissions = [
            ('Can_administrate_lib', 'User can administrate the library'),
            ('Can_add_object', 'User can administrate DB')
        ]

    ordering = ['district_name']

    def __str__(self):
        return self.district_name