from django.urls import path
from . import views


urlpatterns = [
    path('', views.Journeys.as_view(), name='journeys'),
    path('<uuid:journey_id>', views.SingleJourney.as_view(), name='single-journey'),
    path('<uuid:journey_id>/sections', views.JourneySections.as_view(), name='journey-sections'),
]