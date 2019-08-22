from django.urls import path
from . import views

urlpatterns = [
    path('contacts/', views.ContactsView.as_view(), name="contacts"),
    path('contacts/<int:contact_id>', views.ContactsView.as_view(), name="contacts")
] 