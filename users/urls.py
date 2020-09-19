from django.urls import path
<<<<<<< HEAD
from . import views

app_name = "users"

urlpatterns = [
    path("", views.UsersView.as_view()),
    path("me/", views.MeView.as_view()),
    path("me/favs/", views.FavsView.as_view()),
    path("<int:pk>/", views.user_detail),
]
=======

app_name = "users"

urlpatterns = []
>>>>>>> cc2656b759cba23d39d51007debe9d5b6390a042
