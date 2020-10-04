from django.urls import path,include

from . import views

urlpatterns = [
    path('', views.all_job),
    path('<int:id>', views.job_detais),
]