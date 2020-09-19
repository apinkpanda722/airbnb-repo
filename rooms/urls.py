from django.urls import path
<<<<<<< HEAD
from . import views

app_name = "rooms"

urlpatterns = [
    path("list/", views.RoomsView.as_view()),
    path("<int:pk>/", views.RoomView.as_view()),
]
=======

app_name = "rooms"

urlpatterns = []
>>>>>>> cc2656b759cba23d39d51007debe9d5b6390a042
