from django.shortcuts import render
from django.views.generic.base import TemplateView

import time
from datetime import date, timedelta
# Create your views here.


MONTHS = ["januar", "februar", "mars", "april", "mai", "juni",
          "juli", "august", "september", "oktober", "november", "desember"]
WEEKDAYS = ["måndag", "tysdag", "onsdag", "torsdag", "fredag",
            "laurdag", "sundag"]


class DayView(TemplateView):
    template_name = "today.html"

    def get_context_data(self, **kwargs):
        today = date(kwargs['year'], kwargs['month'], kwargs['day']) \
            if (len(kwargs) > 0) else date.today()

        context = super().get_context_data(**kwargs)
        context["week"] = today.isocalendar()[1]
        context["ordinal_day"] = int(today.strftime("%j"))
        context["month"] = MONTHS[today.month - 1]
        context["day"] = today.day
        context["weekday"] = WEEKDAYS[today.isoweekday() - 1]
        context["full_slots"] = [x for x in range(today.isoweekday())]
        context["empty_slots"] = [x for x in range(7 - today.isoweekday())]
        return context
