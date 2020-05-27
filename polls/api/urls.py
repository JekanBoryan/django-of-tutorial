from django.urls import path

from . import views

app_name = "api_polls"
urlpatterns = [
    path('questions', views.PollView.as_view()),
    path('questions/<int:pk>', views.SinglePollView().as_view()),
    path('choices', views.ChoiceView().as_view()),
    path('choices/<int:pk>', views.SingleChoiceView().as_view()),
]
