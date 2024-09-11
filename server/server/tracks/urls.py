
from django.urls import path
from .views import RecommendationApi

app_name = 'tracks'
urlpatterns = [
    path('tracks/<str:name>/', RecommendationApi.as_view()),
]