from django.urls import path
from . import views


urlpatterns = [
    path("", views.CaffeinIntakes.as_view()),
    path("predict/", views.CaffeinePredictionAPIView.as_view(),
         name="predict-caffeine"),
]
