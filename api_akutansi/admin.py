from django.contrib import admin
from api_akutansi.models import DataPembayaran, GajiStaff, GajiGuru

# Register your models here.
admin.site.register(DataPembayaran)
admin.site.register(GajiStaff)
admin.site.register(GajiGuru)