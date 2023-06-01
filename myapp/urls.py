from django.urls import path
from . import views
urlpatterns = [
    path('', views.index, name='my-view'),
    path('getVideo/',views.get_random_video,name='getVideo'),
]