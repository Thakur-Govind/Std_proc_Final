from django.urls import path
from . import views
urlpatterns = [
    path('graph1',views.plotbar, name = 'analyse1'),
]
