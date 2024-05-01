from django.urls import path
from project.constants import ROOT
from project.views import app

app_name = "app"

urlpatterns = [
    path(ROOT, app.index, name="index"),
    path("login/", app.login, name="login"),
    path("register/", app.register, name="register"),
    path("register-label/", app.register_label, name="register-label"),
    path("dashboard/", app.dashboard, name="dashboard"),
    path("subscription/", app.subscription, name="subscription"),
    path("player/", app.player, name="player"),
]