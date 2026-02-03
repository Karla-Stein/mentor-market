from django.urls import path
from . import views


urlpatterns = [
    path('book-a-slot/<int:pk>', views.book_a_slot,
         name='book_a_slot_with'),
    path('my-booking-details/', views.booking_details,
         name='booking_details'),
]
