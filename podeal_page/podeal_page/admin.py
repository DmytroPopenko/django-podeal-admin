from .models import User, Locations, Referrals, Team

from django.contrib import admin

@admin.register(Referrals)
class ReferralsAdmin(admin.ModelAdmin):
    list_display = ('id', 'referrer_info', 'invited_user_info', 'score_for_invite', 'is_accepted')
    list_filter = ('is_accepted', 'score_for_invite')
    search_fields = (
        'user__user_name', 'user__user_surname',
        'invited_user__user_name', 'invited_user__user_surname'
    )

    def referrer_info(self, obj):
        return f"{obj.user.user_name} {obj.user.user_surname}"

    referrer_info.short_description = 'Referrer'

    def invited_user_info(self, obj):
        return f"{obj.invited_user.user_name} {obj.invited_user.user_surname}"

    invited_user_info.short_description = 'Invited User'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ('user_id', 'full_name', 'role', 'is_active', 'custom_id')
    list_filter = ('is_active', 'role', 'team')
    search_fields = ('user_name', 'user_surname', 'custom_id', 'role')
    list_select_related = ('team',)

    def full_name(self, obj):
        return f"{obj.user_name} {obj.user_surname}"

    full_name.short_description = 'Full Name'

admin.site.register(Locations)
admin.site.register(Team)
