from . import views
from django.urls import path


urlpatterns = [
    path('', views.ProfileList.as_view(), name='home'),
    path('availability/', views.set_mentor_availability, name="availability"),
    path('delete-profile/<slug:slug>/', views.profile_delete,
         name='profile_delete'),
    path('edit-availability/<int:pk>', views.edit_availability,
         name='edit_availability'),
    path('edit-profile/', views.edit_profile,
         name='edit_profile'),
    path('my-profile/', views.set_mentor_profile, name="profile"),
    path('<slug:slug>/', views.profile_detail, name='profile_detail'),
]
