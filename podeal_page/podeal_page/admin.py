from django.contrib import admin
from .models import User, Locations, Referrals, Team

admin.site.register(User)
admin.site.register(Locations)
admin.site.register(Referrals)
admin.site.register(Team)