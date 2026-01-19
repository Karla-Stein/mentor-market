from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProfileList.as_view(), name='home'),
    path('availability/', views.set_mentor_availability, name="availability"),
    path('my-profile/', views.set_mentor_profile, name="profile"),
    path('<slug:slug>/', views.profile_detail, name='profile_detail'),
]
