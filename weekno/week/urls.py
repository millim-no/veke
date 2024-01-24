from django.urls import path
from .views import DayView

urlpatterns = [
    path("index.html", DayView.as_view())
]