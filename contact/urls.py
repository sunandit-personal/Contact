from django.urls import path
from . import views

urlpatterns = [
    path('', views.list_contact, name='contact_list'),
    path('add/', views.add_contact, name='add_contact'),
    path('get/<int:pk>/', views.contact_detail, name='contact_detail'),
    path('edit/<int:pk>/', views.edit_contact, name='edit_contact'),
    path('delete/<int:pk>/', views.delete_contact, name='delete_contact'),
    path(
        "contact",
        views.ContactView.as_view(),
        name="contact"
    ),
    path('contact_list/', views.ContactList.as_view()),
]