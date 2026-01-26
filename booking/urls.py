from . import views
from django.urls import path


urlpatterns = [
    path('book-a-slot/<int:pk>', views.book_a_slot,
         name='book_a_slot_with'),
]

