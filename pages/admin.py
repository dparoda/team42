from django.contrib import admin
from .models import *
# Register your models here.

admin.site.site_header = "Team42, System Config"
admin.site.site_title = "Team42"
admin.site.index_title = "Welcome to Sys Config"

admin.site.register(Tblrooms)
admin.site.register(Tblassets)
admin.site.register(Tblnodes)
admin.site.register(Tblbadges)
admin.site.register(Tbllocationdata)