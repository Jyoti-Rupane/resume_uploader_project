from django.urls import path
from resume import views

urlpatterns = [
    path('resume/', views.ProfileView.as_view(), name='resume'),
    path('list/', views.ProfileView.as_view(), name='list')
]
