"""predictor URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from django.urls import path, include
from django.views.generic.base import TemplateView

from games.views import away_wins,home_wins,home_loose,privacy,away_goals,home_goals,now,away_loose,sure_bet,under_goals,to_win,over_goals,raw_predictions,top_pick,vip,gold

urlpatterns = [
    path('admin/', admin.site.urls),
    path('homewin/', home_wins, name="home_wins"),
    path('awaywin/', away_wins, name="away_wins"),
    path('awaygoals/', away_goals, name="away_goals"),
    path('homegoals/', home_goals, name="home_goals"),
    path('homeloose/', home_loose, name="home_loose"),
    path('', now, name="now"),
    path('privacy', privacy, name="privacy"),
    path('awayloose/', away_loose, name="away_loose"),
    path('undergoals/', under_goals, name="under_goals"),
    path('overgoals/', over_goals, name="over_goals"),
    path('predictions/', raw_predictions, name="raw_predictions"),
    path('top-pick', top_pick, name="top_pick"),
    path('to-win/', to_win, name="to_win"),
    path('vip/', vip, name="vip"),
    path('surebet/', sure_bet, name="surebet"),
    path('gold/', gold, name="gold"),
]



if settings.DEBUG:
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)