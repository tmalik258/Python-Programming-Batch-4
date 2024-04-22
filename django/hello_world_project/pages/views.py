from django.shortcuts import render, HttpResponse
from django.views.generic import TemplateView

# Create your views here.

def homePageView(request):
    return render(request, 'pages/home.html')


def aboutPageView(request):
    return render(request, 'pages/about.html')


class ContactPageClassView(TemplateView):
    template_name = 'pages/contact.html'