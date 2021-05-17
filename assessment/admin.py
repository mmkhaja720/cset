from django.contrib import admin
from .models.assessment import Assessment
from .models.user import User
from .models.demography import Demography
# Register your models here.
admin.site.register(Assessment)
admin.site.register(User)
admin.site.register(Demography)