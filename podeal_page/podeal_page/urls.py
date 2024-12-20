"""
URL configuration for podeal_page project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/5.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, re_path
from django.views.static import serve

from podeal_page import settings
from podeal_page.views import UserStatisticsView

urlpatterns = [
    path('admin/', admin.site.urls),
    path("api/v1/users-stats/", UserStatisticsView.as_view()),
    re_path(r'^staticfiles/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),

]
