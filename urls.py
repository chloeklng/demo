from django.urls import path
from .views import home, matching_candidate, matching_job, dashboard

urlpatterns = [
    path('', home),
    path('home/', home, name='home'),
    path('matching_job/', matching_job, name='matching_job'),
    path('matching_candidate/', matching_candidate, name='matching_candidate'),
    path('dashboard/', dashboard, name='dashboard'),
]
