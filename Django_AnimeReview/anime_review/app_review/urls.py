from django.urls import path
from .views import HomePage, AboutPage, AnimePage
from . import views

urlpatterns = [
    path('', HomePage,name='home-page'),
    # path('/about', AboutPage,name='about-page'),


]
