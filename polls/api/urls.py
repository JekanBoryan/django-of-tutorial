from django.urls import path

from . import views

app_name = "api_polls"
urlpatterns = [
    path('', views.PollView.as_view()),
    path('questions/<int:pk>', views.SinglePollView().as_view()),
    path('choices', views.ChoiceCreateView().as_view()),
]
