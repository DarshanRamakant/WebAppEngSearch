from django.contrib import admin

# Register your models here.
from .models import CollegeDB, BranchDB , SeatMetrixDb

admin.site.register(CollegeDB)
admin.site.register(BranchDB)
admin.site.register(SeatMetrixDb)