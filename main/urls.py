from django.urls import path,include
from enricbd import views


urlpatterns = [
    path('enric', views.EnricApi.as_view()),
]
