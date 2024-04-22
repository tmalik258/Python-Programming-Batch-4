from django.urls import path

from .views import homePageView, aboutPageView, ContactPageClassView


urlpatterns = [
    # path("", homePageView, name="home"),
    path("about/", aboutPageView, name="about"),
    path('contact/', ContactPageClassView.as_view(), name="contact")
]