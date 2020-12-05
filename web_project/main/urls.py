from django.urls import path
from . import views
from django.conf.urls import url ,include





urlpatterns = [
    path('',views.index, name='AnimeHome'),
    path('genres',views.genres, name='Genres'),
    path('games',views.games, name='Games'),
    path('registration',views.registration, name='registration'),

    url(r'^register/$', views.RegisterFormView.as_view()),
    url(r'^login/$', views.LoginFormView.as_view()),
    url(r'^logout/$', views.LogoutFormView.as_view()),
    url(r'^registration/$', views.RegistrationFormView.as_view()),
] 