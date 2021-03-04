from django.shortcuts import render
from django.http import HttpResponse
from .models import Tutorial,TutorialCategory, TutorialSeries
from django.contrib.auth.forms import UserCreationForm

def single_slug(request, single_slug):
    categories = [c.category_slug for c in TutorialCategory.objects.all()]
    if single_slug in categories:
        matching_series = TutorialSeries.objects.filter(tutorial_category__category_slug=single_slug)
        series_urls = {}

        for m in matching_series.all():
            part_one = Tutorial.objects.filter(tutorial_series__tutorial_series=m.tutorial_series).earliest("tutorial_published")
            series_urls[m] = part_one.tutorial_slug

        return render(request=request,
                      template_name='main/category.html',
                      context={"tutorial_series": matching_series, "part_ones": series_urls})



# Create your views here.
def home(request):
    return render(request = request,
                  template_name='main/categories.html',
                  context = {"tutorials":Tutorial.objects.all})


def register(request):
    form = UserCreationForm
    return render(request = request,
                  template_name = "main/register.html",
                  context={"form":form})
