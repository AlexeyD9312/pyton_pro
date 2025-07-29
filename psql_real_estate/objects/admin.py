from django.contrib import admin
from .models import District


@admin.register(District)
class DistrictAdmin(admin.ModelAdmin):
    list_display = ['district_ID','city_ID','district_name','is_admin_district']
    list_filter = ['city_ID', 'is_admin_district']
    search_fields = ['district_name']
    ordering = ['district_name']
    list_per_page = 15
    list_editable = ['is_admin_district',]

    fieldsets = (
        ('General information',{
            'fields' : ['district_ID','district_name']
        }),
        ('Images', {
            'fields': ['image'],
            'description' : 'download images'
        })
    )

    def clean(self):
        super().clean()
        if len(self.district_name) > 100:
            raise ValidationError('Use more short name')



