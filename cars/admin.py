from django.contrib import admin
from .models import SeftyFeature
# Register your models here.
admin.site.register(SeftyFeature)
class SeftyFeatureAdmin(admin.ModelAdmin):
    list_display=['car_type','safety_features','registration']
