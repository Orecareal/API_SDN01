from django.contrib import admin
from api_staf.models import DataStaff, DataKelas, DataKeuangan, DataBerita

# Register your models here.
admin.site.register(DataStaff)
admin.site.register(DataKelas)
admin.site.register(DataKeuangan)
admin.site.register(DataBerita)