from django.shortcuts import render
from django.views.generic.base import TemplateView

# Create your views here.

class DayView(TemplateView):
    template_name = "today.html"

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        print(dir(self.request))
        #context["latest_articles"] = Article.objects.all()[:5]
        return context
