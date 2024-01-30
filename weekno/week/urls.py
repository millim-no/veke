from django.urls import path
from .views import DayView

urlpatterns = [
    path("", DayView.as_view(), name="today"),
    path("<int:year>/<int:month>/<int:day>", DayView.as_view(), name="by_day"),
]
