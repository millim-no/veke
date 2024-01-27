from django.urls import path
from .views import DayView

urlpatterns = [
    path("", DayView.as_view())
]
