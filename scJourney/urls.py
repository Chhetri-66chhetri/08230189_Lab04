from django.urls import path
from . import views

urlpatterns = [
    path('index.html', views.index, name='index'),      # home page accessible at /index.html
    path('aboutMe.html', views.aboutMe, name='aboutMe'),  # about page accessible at /aboutMe.html
    path('', views.index),                               # optional: also make / go to index
]
