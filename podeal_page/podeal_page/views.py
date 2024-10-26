from django.http import JsonResponse
from django.views import View
from .models import User, Referrals
from django.db.models import Count, Sum, Q


class UserStatisticsView(View):
    def get(self, request, *args, **kwargs):
        result = User.objects.aggregate(
            all=Count('pk', distinct=True),
            active=Count('pk', filter=Q(is_active=True), distinct=True),
            invited=Count('referrals', filter=Q(referrals__is_accepted=True))
        )
        data = {"all": result["all"], "active": result["active"], "invited": result["invited"]}
        return JsonResponse(data)
