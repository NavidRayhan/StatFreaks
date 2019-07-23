from django.contrib import admin
from .models import Single_Season, Basic_Stats, Advanced_Stats
# Register your models here.
admin.site.register(Advanced_Stats)
admin.site.register(Basic_Stats)
admin.site.register(Single_Season)

